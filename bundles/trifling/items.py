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

git_sha = node.metadata.get('trifling', {}).get('git_sha', 'main')

actions = {
    'clone_trifling': {
        'command': 'git clone https://github.com/zellyn/trifling /opt/trifling/src || true',
        'unless': 'test -d /opt/trifling/src/.git',
        'needs': [
            'pkg_apt:git',
            'directory:/opt/trifling',
        ],
    },
    'update_and_build_trifling': {
        'command': (
            f'cd /opt/trifling/src && '
            f'git fetch origin && '
            f'git checkout {git_sha} && '
            f'/usr/bin/go build -o /opt/trifling/trifling'
        ),
        'unless': (
            f'test -f /opt/trifling/trifling && '
            f'go version -m /opt/trifling/trifling | grep -q "vcs.revision={git_sha}"'
        ),
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
            'action:update_and_build_trifling',
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
