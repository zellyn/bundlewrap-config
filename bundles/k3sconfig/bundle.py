"""
K3s cluster configuration and manifests.

Manages Kubernetes manifests and configuration for k3s clusters.

Required metadata (for nodes using this bundle):
  - k3sconfig/email: Email address for cert-manager and other configs

Example metadata:
    'k3sconfig': {
        'email': 'admin@example.com',
    }

Note: This bundle is separate from the k3s bundle which manages the k3s binary
and service itself.
"""
