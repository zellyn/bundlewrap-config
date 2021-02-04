# Copied from https://git.sr.ht/~bfiedler/bundlewrap/tree/main/item/bundles/apt

pkg_apt = {}

actions = {
    'apt-update': {
        'command': 'apt-get update',
        'needed_by': {'pkg_apt:'},
        'triggered': True,
        'cascade_skip': False,
    }
}

files = {
    # '/etc/apt/sources.list': {
    #     'triggers': {'action:apt-update'},
    # },

    # '/etc/apt/preferences.d/releases.pref': {},
    # '/etc/apt/preferences.d/packages.pref': {
    #     'content_type': 'mako',
    # },

    '/etc/apt/apt.conf.d/90recommended-packages': {}
}

if node.metadata.get('apt/autoupgrade', True):
    pkg_apt['unattended-upgrades'] = {}
    files['/etc/apt/apt.conf.d/10periodic'] = {}

directories = {
    '/etc/apt/sources.list.d': {
        # TODO: enable purging once all files are under bw's control
        'purge': node.metadata.get('apt/managed-by-bw', False),
    },
    '/etc/apt/preferences.d': {
        # TODO: enable purging once all files are under bw's control
        'purge': node.metadata.get('apt/managed-by-bw', False),
    },
}

for name, repos in node.metadata.get('apt/repos', {}).items():
    files['/etc/apt/sources.list.d/{}.list'.format(name)] = {
        'content': '\n'.join(repos)+'\n',
        'triggers': {
            'action:apt-update',
        },
    }

for package, options in node.metadata.get('apt/packages', {}).items():
    pkg_apt[package] = options
