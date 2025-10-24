"""
Automated backup system for external disk.

Backs up minecraft and trifling data to an external disk weekly.
The external disk is kept unmounted except during backups for safety.

Required metadata:
  - backups/external_uuid: UUID of external backup disk
  - backups/external_mount: Mount point for external disk (e.g., '/mnt/external')
  - backups/minecraft_source: Path to minecraft backups directory
  - backups/trifling_source: Path to trifling data directory

Example metadata:
    'backups': {
        'external_uuid': 'c690eaa6-a19e-43d5-886f-c468a738ddc9',
        'external_mount': '/mnt/external',
        'minecraft_source': '/home/zellyn/minecraftbe/survivalone/backups',
        'trifling_source': '/opt/trifling/data',
    }

Schedule: Monday at 00:00 (midnight Sunday/Monday)
"""
