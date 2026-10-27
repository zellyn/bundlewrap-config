linger_users = node.metadata.get('ssh-agent', {}).get('linger_users', [node.username])

files = {
    '/etc/systemd/user/ssh-agent.service': {
        'source': 'ssh-agent.service',
        'mode': '0644',
    },
    '/etc/profile.d/ssh-agent.sh': {
        'content': '# Managed by bundlewrap\nexport SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"\n',
        'mode': '0644',
    },
    '/etc/ssh/ssh_config.d/50-add-keys-to-agent.conf': {
        'content': '# Managed by bundlewrap\nAddKeysToAgent yes\n',
        'mode': '0644',
    },
}

# Equivalent to `systemctl --global enable ssh-agent.service`
directories = {
    '/etc/systemd/user/default.target.wants': {
        'mode': '0755',
    },
}

symlinks = {
    '/etc/systemd/user/default.target.wants/ssh-agent.service': {
        'target': '/etc/systemd/user/ssh-agent.service',
        'needs': [
            'file:/etc/systemd/user/ssh-agent.service',
            'directory:/etc/systemd/user/default.target.wants',
        ],
    },
}

actions = {
    f'enable_linger_{user}': {
        'command': f'loginctl enable-linger {user}',
        'unless': f'test -f /var/lib/systemd/linger/{user}',
    }
    for user in linger_users
}
