"""
Keepalived for high availability virtual IPs.

Manages keepalived service and configuration for VRRP virtual IP addresses.

Required metadata:
  - keepalived/virtual_ipaddress: The virtual IP address to manage
  - keepalived/virtual_router_id: VRRP router ID (must be unique on network, 1-255)

Example metadata:
    'keepalived': {
        'virtual_ipaddress': '192.168.7.42',
        'virtual_router_id': 43,
    }

Note: All nodes in the same keepalived group should have the same virtual_router_id
and virtual_ipaddress. The router with the highest priority becomes master.
"""
