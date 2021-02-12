groups = {
    #'group-1': {
    #    'bundles': (
    #        'bundle-1',
    #    ),
    #    'members': (
    #        'node-1',
    #    ),
    #    'subgroups': (
    #        'group-2',
    #    ),
    #},
    'all': {
        'member_patterns': (
            r".*",
        ),
        'bundles': ["apt"]
    },
    'katespi': {
        'os': 'ubuntu',
        'metadata': {
            'apt': {
                'repos': {
                    'tailscale': [
                        '# Managed by bundlewrap',
                        '# Tailscale packages for ubuntu groovy',
                        'deb https://pkgs.tailscale.com/stable/ubuntu groovy main',
                    ],
                },
            },
        },
        'bundles': [
            'keepalived',
        ],
    },
    'raspi': {
        'os': 'raspbian',
        'metadata': {
            'apt': {
                'repos': {
                    'tailscale': [
                        '# Managed by bundlewrap',
                        '# Tailscale packages for raspbian buster',
                        'deb https://pkgs.tailscale.com/stable/raspbian buster main',
                    ],
                },
            },
        },
    },
}
