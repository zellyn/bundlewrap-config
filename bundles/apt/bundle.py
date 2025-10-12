"""
APT package management and configuration.

Manages unattended upgrades, package sources, and apt preferences.

Optional metadata:
  - apt/autoupgrade: Enable unattended-upgrades (default: True)
  - apt/managed-by-bw: Purge unmanaged files in sources.list.d and preferences.d (default: False)
  - apt/repos: Dict of additional apt repositories
  - apt/packages: Dict of packages to install with options

Example metadata:
    'apt': {
        'autoupgrade': True,
        'managed-by-bw': False,
        'repos': {
            'docker': [
                'deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable',
            ],
        },
        'packages': {
            'docker-ce': {},
        },
    }

Note: This bundle is applied to all nodes via the 'all' group.
"""
