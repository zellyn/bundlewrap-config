nodes = {
    'katespi1': {
        'hostname': 'ubuntu@100.64.111.50',
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
        'hostname': 'ubuntu@100.125.197.24',
        'groups': {'katespi', 'k3s'},
    },
    'katespi3': {
        'hostname': 'ubuntu@100.109.141.36',
        'groups': {'katespi', 'k3s'},
    },
    'katespi4': {
        'hostname': 'ubuntu@100.100.221.82',
        'groups': {'katespi', 'k3s'},
    },
    'pizero': {
        'hostname': 'pi@100.78.213.45',
        'groups': {'raspi'},
    },
    'casepi': {
        'hostname': 'ubuntu@100.106.232.102',
        'groups': {'ubuntu'},
        'bundles': [
            'ddclient',
        ],
    },
    'lenovo': {
        'hostname': '100.76.94.91',
        'username': 'zellyn',
        'groups': {'ubuntu'},
        'bundles': [
#            'ddclient',
        ],
        'metadata': {
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
