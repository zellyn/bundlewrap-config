external_uuid = node.metadata.get('backups', {}).get('external_uuid', '')
external_mount = node.metadata.get('backups', {}).get('external_mount', '/mnt/external')

# Add external disk to fstab with noauto option (only mount when needed)
actions = {
    'add_external_to_fstab': {
        'command': f'echo "UUID={external_uuid} {external_mount} ext4 noauto,defaults 0 2" >> /etc/fstab',
        'unless': f'grep -q "UUID={external_uuid}" /etc/fstab',
    },
}

directories = {
    external_mount: {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    },
}

files = {
    '/usr/local/bin/backup.sh': {
        'source': 'backup.sh',
        'content_type': 'mako',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    },
    '/etc/systemd/system/backup.service': {
        'source': 'backup.service',
        'mode': '0644',
        'triggers': [
            'action:systemd-reload',
        ],
    },
    '/etc/systemd/system/backup.timer': {
        'source': 'backup.timer',
        'mode': '0644',
        'triggers': [
            'action:systemd-reload',
        ],
    },
}

# Enable and start the timer (not the service itself)
svc_systemd = {
    'backup.timer': {
        'enabled': True,
        'running': True,
        'needs': [
            'file:/etc/systemd/system/backup.service',
            'file:/etc/systemd/system/backup.timer',
            'file:/usr/local/bin/backup.sh',
        ],
    },
}
