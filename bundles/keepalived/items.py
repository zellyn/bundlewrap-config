pkg_apt = {
    'keepalived': {
        'when_creating': {
            'start_service': False,
        },
    },
}

svc_systemd = {
    'keepalived.service': {
        'needs': [
            'file:/etc/keepalived/keepalived.conf',
        ],
    },
}

files = {
    '/etc/keepalived/keepalived.conf': {
        'triggers': [
            'svc_systemd:keepalived.service:reload',
        ],
    },
}
