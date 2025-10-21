pkg_apt = {
    'golang-go': {},
    'git': {},
}

users = {
    'trifling': {
        'home': '/opt/trifling',
        'shell': '/usr/sbin/nologin',
    },
}

directories = {
    '/opt/trifling': {
        'owner': 'trifling',
        'group': 'trifling',
        'mode': '0755',
        'needs': ['user:trifling'],
    },
}

actions = {
    'clone_trifling': {
        'command': 'git clone https://github.com/zellyn/trifling /opt/trifling/src || (cd /opt/trifling/src && git pull)',
        'unless': 'test -d /opt/trifling/src/.git',
        'needs': [
            'pkg_apt:git',
            'directory:/opt/trifling',
        ],
    },
    'build_trifling': {
        'command': 'cd /opt/trifling/src && /usr/bin/go build -o /opt/trifling/trifling',
        'needs': [
            'pkg_apt:golang-go',
            'action:clone_trifling',
        ],
        'triggers': [
            'svc_systemd:trifling.service:restart',
        ],
    },
}

files = {
    '/etc/default/trifling': {
        'source': 'trifling.env',
        'content_type': 'mako',
        'mode': '0600',
        'triggers': [
            'svc_systemd:trifling.service:restart',
        ],
    },
    '/etc/systemd/system/trifling.service': {
        'content_type': 'mako',
        'triggers': [
            'action:systemd-reload',
        ],
        'needs': [
            'action:build_trifling',
        ],
    },
}

svc_systemd = {
    'trifling.service': {
        'needs': [
            'file:/etc/systemd/system/trifling.service',
            'file:/etc/default/trifling',
        ],
    },
}
