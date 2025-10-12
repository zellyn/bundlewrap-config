"""
Dynamic DNS client for Cloudflare.

Updates DNS records when your public IP address changes.

Required metadata:
  - ddclient/login: Email for Cloudflare account
  - ddclient/protocol: Should be 'cloudflare'
  - ddclient/password: Encrypted Cloudflare API token (with Zone:DNS:Edit permissions)
  - ddclient/zone: Domain name (e.g., 'example.com')
  - ddclient/records: DNS record(s) to update (e.g., 'subdomain.example.com')

Example metadata:
    'ddclient': {
        'login': 'user@example.com',
        'protocol': 'cloudflare',
        'password': 'encrypt$...',
        'zone': 'example.com',
        'records': 'subdomain.example.com',
    }

Cloudflare API token can be created at:
https://dash.cloudflare.com/profile/api-tokens
Required permissions: Zone > DNS > Edit for specific zone
"""
