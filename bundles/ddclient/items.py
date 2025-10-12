pkg_apt = {
    'ddclient': {
        'when_creating': {
            'start_service': False,
        },
    },
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
        'mode': '0600',
        'content_type': 'mako',
        'triggers': [
            'svc_systemd:ddclient.service:restart',
        ],
    },
    '/etc/default/ddclient': {
        'source': 'default-ddclient',
        'mode': '0644',
        'triggers': [
            'svc_systemd:ddclient.service:restart',
        ],
    },
}
