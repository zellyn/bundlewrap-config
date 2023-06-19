nodes = {
    'katespi1': {
        'hostname': 'ubuntu@100.89.32.19',
        'groups': {'katespi', 'k3s'},
        'bundles': {'k3sconfig'},
        'metadata': {
            'k3s': {
                'server': True,
            },
            'k3sconfig': {
                'email': 'zellyn@gmail.com',
            },
        },
    },
    'katespi2': {
        'hostname': 'ubuntu@100.113.249.70',
        'groups': {'katespi', 'k3s'},
    },
    'katespi3': {
        'hostname': 'ubuntu@100.88.221.38',
        'groups': {'katespi', 'k3s'},
    },
    'katespi4': {
        'hostname': 'ubuntu@100.109.4.116',
        'groups': {'katespi', 'k3s'},
    },
    'pizero': {
        'hostname': 'pi@100.78.213.45',
        'groups': {'raspi'},
    },
    'casepi': {
        'hostname': 'ubuntu@100.112.123.101',
        'groups': {'ubuntu'},
        'bundles': [
            'ddclient',
        ],
        'metadata': {
            'apt': {
                'repos': {
                    'tailscale': [
                        '# Managed by bundlewrap',
                        '# Tailscale packages for ubuntu impish',
                        'deb https://pkgs.tailscale.com/stable/ubuntu impish main',
                    ],
                },
            },
        },
    },
    'lenovo': {
        'hostname': 'zellyn@lenovo',
        'groups': {'ubuntu'},
        'bundles': [
            'ddclient',
        ],
        'metadata': {
            'apt': {
                'repos': {
                    'tailscale': [
                        '# Managed by bundlewrap',
                        '# Tailscale packages for ubuntu focal',
                        'deb [signed-by=/usr/share/keyrings/tailscale-archive-keyring.gpg] https://pkgs.tailscale.com/stable/ubuntu focal main'
                    ],
                },
            },
            'ddclient': {
                'login': 'zellyn@gmail.com',
                'protocol': 'cloudflare',
                'password': 'encrypt$gAAAAABiJ2G5Lis8zzE3aY19jk0A6ys64ZAIbFVYXgaIV7e848QeZ0nPlryFV2Vmzwqt4hdCaLznKyIwJvyD-AZoTLeWEgfX13smrQgWOA-5K7jlvhaphi5TP--CGbhTU4GDGSLQZmGC',
                'zone': 'greenseptember.com',
                'records': 'minecraft.greenseptember.com',
            },
        },
    },
}
