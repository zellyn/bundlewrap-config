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
                'version': 'v1.31.4+k3s1',  # Default version for all k3s nodes (latest stable)
            }
        },
        'bundles': [
            'k3s',
        ],
    },
    'katespi': {
        'os': 'ubuntu',
        'metadata': {
            'keepalived': {
                'virtual_ipaddress': '192.168.7.42',
                'virtual_router_id': 43,
            },
        },
        'bundles': [
            'keepalived',
        ],
    },
    'ubuntu': {
        'os': 'ubuntu',
    },
    'raspi': {
        'os': 'raspbian',
    },
}
