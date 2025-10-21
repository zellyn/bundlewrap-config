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
            'systemd',
            'trifling',
        ],
        'metadata': {
            'ddclient': {
                'login': 'token',
                'protocol': 'cloudflare',
                'password': 'encrypt$gAAAAABo6sk_Vt16GqniEc79YjDV8t_vHwJjRTPK4W1Z2hP0kWa3Frav15kszt3i3y8eV0VGDBPXlivgWhFZQQ-EXaMMV9ZyQZViMZUOHf2fxoRcd3fGrCbYBpQ2RNaXq-usR3BBdyAg',
                'zones': [
                    {
                        'zone': 'greenseptember.com',
                        'records': 'minecraft.greenseptember.com',
                    },
                    {
                        'zone': 'trifling.org',
                        'records': 'trifling.org',
                    },
                ],
            },
            'caddy2': {
                'sites': {
                    'trifling': {
                        'domain': 'trifling.org',
                        'proxy_to': 'localhost:3000',
                        'email': 'zellyn@gmail.com',
                    },
                },
            },
            'trifling': {
                'google_client_id': 'encrypt$gAAAAABo9v1JCr5PW6Ur7lGMxlwUhzqDdblmKXH9bj89pj1Bz10wLjbVjbS6d125fRFvSnP6Qd55oxADv37xD5QnamVqJdLqeCSg4z5lGkfDEHctUzgORrFiBKKp4fHhaXQsGOdQzeZCPPza2D0h3Y50WTCiMsb36mY5mEaSa2E17l6pIirijMA=',
                'google_client_secret': 'encrypt$gAAAAABo9v0i1Or6_mor0ZcIiaoeXp-JsRAH_6G8li5xR4yHQVibiEukYIyiuXI6e-C29y2liHxumNiTg_-mvM5C2LmU-d7r50SLm51ClQnl3JIHkigto7lSquGa0ywwZQec80Fb6-UT',
                'oauth_redirect_url': 'https://trifling.org/auth/callback',
                'port': 3000,
            },
        },
    },
}
