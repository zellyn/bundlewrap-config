# Get or create a token for the cluster to use
token = node.metadata['k3s'].get('k3s_token', repo.vault.password_for("k3s"))

# Server names things differently from agent, so we need some different context.
if node.metadata['k3s']['server']:
    service = 'k3s.service'
    context = {
        'service_file': '/etc/systemd/system/k3s.service',
        'service_type': 'notify',
        'params': 'server',
        'token': token,
    }
else:
    service = 'k3s-agent.service'

    # Find the node with server=True, and use its IP/hostname in K3S_URL
    server = [node for node in repo.nodes_in_group('k3s') if node.metadata['k3s']['server']][0]
    server_hostname = server.hostname.split('@')[-1]
    k3s_url = 'https://%s:6443' % server_hostname

    context = {
        'service_file': '/etc/systemd/system/k3s-agent.service',
        'service_type': 'exec',
        'params': 'agent',
        'token': token,
        'k3s_url': k3s_url,
    }

# The systemd service.
svc_systemd = {
    service: {
        'enabled': True,
        'running': True,
        'needs': [
            'file:/usr/local/bin/k3s',
            'file:' + context['service_file'],
            'file:' + context['service_file']+'.env',
        ],
    },
}

files = {
    # The binary. Run get_k3s in the root to get the latest, then copy it to
    # bundles/k3s/files/k3s (symlink didn't work 😞)
    '/usr/local/bin/k3s': {
        'source': 'k3s',
        'content_type': 'binary',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    },
    context['service_file']: {
        'content_type': 'mako',
        'context': context,
        'mode': '0664',
        'source': 'server-or-agent.service.mako',
    },
    context['service_file']+'.env': {
        'content_type': 'mako',
        'context': context,
        'mode': '0400',
        'source': 'server-or-agent.service.env.mako',
    },
    # I just copied /boot/firmware/cmdline.txt and pasted the memory cgroup
    # stuff k3s wanted on the end. This needs a reboot before it takes effect,
    # but I haven't set that up yet.
    '/boot/firmware/cmdline.txt': {
        'content': 'dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=LABEL=writable rootfstype=ext4 elevator=deadline rootwait fixrtc quiet splash cgroup_memory=1 cgroup_enable=memory\n',
        'mode': '0755',
    }
}
