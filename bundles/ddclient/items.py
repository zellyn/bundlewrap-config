pkg_apt = {
    'ddclient': {
        'when_creating': {
            'start_service': False,
        },
    },
    'libio-socket-ssl-perl': {},
}

svc_systemd = {
    'ddclient.service': {
        'needs': [
            'pkg_apt:',
            'file:/etc/ddclient.conf',
        ],
    },
}

files = {
    '/etc/ddclient.conf': {
        'content_type': 'mako',
        'triggers': [
            'svc_systemd:ddclient.service:restart',
        ],
    },
}
