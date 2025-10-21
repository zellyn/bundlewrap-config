"""
Trifling web application server.

Installs and runs the trifling Go application from https://github.com/zellyn/trifling
as a systemd service.

Required metadata:
  - trifling/google_client_id: Encrypted Google OAuth client ID
  - trifling/google_client_secret: Encrypted Google OAuth client secret
  - trifling/oauth_redirect_url: OAuth redirect URL (e.g., 'https://trifling.org/auth/callback')
  - trifling/port: Port to listen on (default: 3000)

Example metadata:
    'trifling': {
        'google_client_id': 'encrypt$...',
        'google_client_secret': 'encrypt$...',
        'oauth_redirect_url': 'https://trifling.org/auth/callback',
        'port': 3000,
    }
"""
