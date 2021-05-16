actions = {
    'systemd-reload': {
        'command': 'systemctl daemon-reload',
        'cascade_skip': False,
        'triggered': True,
        'needed_by': {
            'svc_systemd:',
        },
    },
}