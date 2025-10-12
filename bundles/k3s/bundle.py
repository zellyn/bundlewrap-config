"""
K3s lightweight Kubernetes distribution.

Uses the official k3s install script to download and install k3s automatically.
Handles both server and agent nodes with proper token management.

Required metadata:
  - k3s/server: Boolean indicating if this is a server (True) or agent (False) node

Optional metadata:
  - k3s/version: K3s version to install (default: 'v1.28.3+k3s1')
  - k3s/k3s_token: Cluster token (defaults to generated password from vault)

Example metadata:
    'k3s': {
        'server': True,  # or False for agent nodes
        'version': 'v1.30.0+k3s1',  # Optional: override default version
    }

How upgrades work:
  - Change k3s/version in metadata
  - Run `bw apply` - the install script will upgrade to the new version
  - The `unless` condition checks installed version to prevent unnecessary reinstalls

Note: Updates /boot/firmware/cmdline.txt for cgroup support.
A reboot is required after first installation for cgroups to take effect.
"""
