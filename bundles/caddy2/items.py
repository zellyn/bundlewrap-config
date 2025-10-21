pkg_apt = {
    'caddy': {},
}

files = {
    '/etc/caddy/Caddyfile': {
        'content_type': 'mako',
        'mode': '0644',
        'triggers': [
            'svc_systemd:caddy.service:restart',
        ],
    },
}

svc_systemd = {
    'caddy.service': {
        'needs': [
            'pkg_apt:caddy',
            'file:/etc/caddy/Caddyfile',
        ],
    },
}
