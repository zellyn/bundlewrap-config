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
    'k3s': {
        'metadata': {
            'k3s': {
                'server': False,
            }
        },
        'bundles': [
            'k3s',
        ],
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
            'ddclient': {
                'login': 'vO5JlDJI7xNaixYL',
                'password': 'encrypt$gAAAAABgJuX3t4fsJpaU52il8Gye8hMSdzKs82I811q10iirsNVOfpCJ-AHG1H4JfgQzGkczX87zXY4c1swtkUBH4NBPHf_Xd6UIIz7QyIYIjEHvQh4GaA4=',
                'domain': 'greenseptember.com',
            },
            'keepalived': {
                'virtual_ipaddress': '192.168.2.42',
                'virtual_router_id': 42,
            },
        },
        'bundles': [
            'keepalived',
            'ddclient',
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
