files = {
    # The binary. Run get_k3s in the root to get the latest, then copy it to
    # bundles/k3s/files/k3s (symlink didn't work 😞)
    '/var/lib/rancher/k3s/server/manifests/traefik-config.yaml': {
        'source': 'traefik-config.yaml',
        'content_type': 'mako',
        'context': {
            'email': node.metadata['k3sconfig']['email']
        },
        'mode': '0600',
        'owner': 'root',
        'group': 'root',
    },
}
