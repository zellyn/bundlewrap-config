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
                        'deb https://pkgs.tailscale.com/stable/ubuntu impish main',
                    ],
                },
            },
            'ddclient': {
                'login': 'zellyn@gmail.com',
                'protocol': 'cloudflare',
                'password': 'encrypt$gAAAAABiJ2G5Lis8zzE3aY19jk0A6ys64ZAIbFVYXgaIV7e848QeZ0nPlryFV2Vmzwqt4hdCaLznKyIwJvyD-AZoTLeWEgfX13smrQgWOA-5K7jlvhaphi5TP--CGbhTU4GDGSLQZmGC',
                'zone': 'greenseptember.com',
                'records': 'greenseptember.com',
            },
            'keepalived': {
                'virtual_ipaddress': '192.168.7.42',
                'virtual_router_id': 43,
            },
        },
        'bundles': [
            'keepalived',
            'ddclient',
        ],
    },
    'ubuntu': {
        'os': 'ubuntu',
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
