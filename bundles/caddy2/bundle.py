"""
Caddy 2 web server with automatic HTTPS.

Installs and configures Caddy 2 as a reverse proxy with automatic TLS certificate management.

Required metadata:
  - caddy2/sites: Dictionary of site configurations
    Each site should have:
      - domain: The domain name
      - proxy_to: Where to proxy requests (e.g., 'localhost:3000')
      - email: Email for Let's Encrypt (optional, for cert notifications)

Example metadata:
    'caddy2': {
        'sites': {
            'trifling': {
                'domain': 'trifling.org',
                'proxy_to': 'localhost:3000',
                'email': 'admin@example.com',
            },
        },
    }
"""
