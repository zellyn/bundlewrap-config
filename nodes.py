nodes = {
    'katespi1': {
        'hostname': 'ubuntu@100.89.32.19',
        'groups': {'katespi', 'k3s'},
        'bundles': {'k3sconfig'},
        'metadata': {
            'k3s': {
                'server': True,
            }
        }
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
        'hostname': 'pi@100.79.85.31',
        'groups': {'raspi'},
    },
}
