nodes = {
    'katespi1': {
        'hostname': 'ubuntu@katespi1',
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
        'hostname': 'ubuntu@katespi2',
        'groups': {'katespi', 'k3s'},
    },
    'katespi3': {
        'hostname': 'ubuntu@katespi3',
        'groups': {'katespi', 'k3s'},
    },
    'katespi4': {
        'hostname': 'ubuntu@katespi4',
        'groups': {'katespi', 'k3s'},
    },
    'pizero': {
        'hostname': 'pi@100.78.213.45',
        'groups': {'raspi'},
    },
    'casepi': {
        'hostname': 'ubuntu@100.106.232.102',
        'groups': {'ubuntu'},
    },
    'lenovo': {
        'hostname': '100.76.94.91',
        'username': 'zellyn',
        'groups': {'ubuntu'},
        'bundles': [
            'ddclient',
            'caddy2',
        ],
        'metadata': {
            'ddclient': {
                'login': 'zellyn@gmail.com',
                'protocol': 'cloudflare',
                'password': 'encrypt$gAAAAABo6sk_Vt16GqniEc79YjDV8t_vHwJjRTPK4W1Z2hP0kWa3Frav15kszt3i3y8eV0VGDBPXlivgWhFZQQ-EXaMMV9ZyQZViMZUOHf2fxoRcd3fGrCbYBpQ2RNaXq-usR3BBdyAg',
                'zone': 'greenseptember.com',
                'records': 'minecraft.greenseptember.com',
            },
        },
    },
}
