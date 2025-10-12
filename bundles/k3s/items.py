# Get k3s version from metadata (updated to v1.31.4+k3s1 which is latest stable as of Oct 2025)
k3s_version = node.metadata.get('k3s/version', 'v1.31.4+k3s1')

# Determine if this is a server or agent node
is_server = node.metadata['k3s']['server']

# For agent nodes, find the server node and create a Fault to get the token
if not is_server:
    server = [n for n in repo.nodes_in_group('k3s') if n.metadata['k3s']['server']][0]
    server_hostname = server.hostname.split('@')[-1]
    k3s_url = f'https://{server_hostname}:6443'

    # Create a Fault to read the token from the server node at runtime
    def get_server_token():
        result = server.run('cat /var/lib/rancher/k3s/server/node-token', may_fail=True)
        if result.return_code != 0:
            # If server token doesn't exist yet, use our pre-generated token
            # This handles first-time installation
            return repo.vault.password_for("k3s")
        # Decode bytes to string and strip whitespace
        token = result.stdout
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        return token.strip()

    from bundlewrap.utils import Fault
    k3s_token = Fault("get k3s server token", get_server_token)
else:
    # For server, use the pre-generated token from vault
    k3s_token = repo.vault.password_for("k3s")

files = {
    '/boot/firmware/current/cmdline.txt': {
        # Ubuntu 25.10 with os_prefix=current/ uses /boot/firmware/current/cmdline.txt
        # IMPORTANT: Must be single line with NO newline at end!
        # Per Raspberry Pi kernel maintainer: cgroup_enable=memory overrides DTB's cgroup_disable=memory
        # Note: cgroup_memory=1 is NOT needed and kernel will complain about it
        'content': 'console=serial0,115200 multipath=off dwc_otg.lpm_enable=0 console=tty1 root=LABEL=writable rootfstype=ext4 panic=10 rootwait fixrtc cgroup_enable=cpuset cgroup_enable=memory',
        'mode': '0755',
    },
}

# For server nodes, create the token file before installation
# This ensures the server uses our pre-generated token
if is_server:
    files['/etc/rancher/k3s-token'] = {
        'content': k3s_token,
        'mode': '0600',
        'owner': 'root',
        'group': 'root',
    }

# Install k3s using the official install script
if is_server:
    install_command = f'K3S_TOKEN="$(cat /etc/rancher/k3s-token)" curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION={k3s_version} sh -s - server'
    install_needs = [
        'file:/boot/firmware/current/cmdline.txt',
        'file:/etc/rancher/k3s-token',
    ]
else:
    # For agents, pass the token directly in the install command
    # Use a Fault-safe approach where the token is evaluated at install time
    install_command = f'K3S_URL="{k3s_url}" K3S_TOKEN="{k3s_token}" curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION={k3s_version} sh -s - agent'
    install_needs = [
        'file:/boot/firmware/current/cmdline.txt',
    ]

actions = {
    'install_k3s': {
        'command': install_command,
        'unless': f'test -x /usr/local/bin/k3s && /usr/local/bin/k3s --version 2>/dev/null | grep -q {k3s_version}',
        'needs': install_needs,
        'cascade_skip': False,
    },
}

# For agent nodes, also create the service.env file with the token
# This ensures the systemd service has the correct token even if the install script doesn't create it properly
if not is_server:
    files['/etc/systemd/system/k3s-agent.service.env'] = {
        'content_type': 'mako',
        'source': 'agent.service.env',
        'context': {
            'k3s_url': k3s_url,
            'k3s_token': k3s_token,
        },
        'mode': '0600',
        'owner': 'root',
        'group': 'root',
        'triggers': [
            'svc_systemd:k3s-agent:restart',
        ],
        'needs': [
            'action:install_k3s',
        ],
    }

# Manage the k3s systemd service
svc_systemd = {
    'k3s' if is_server else 'k3s-agent': {
        'enabled': True,
        'running': True,
        'needs': ['action:install_k3s'],
    },
}
