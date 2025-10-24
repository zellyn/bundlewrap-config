#!/bin/bash
# Managed by bundlewrap
# Weekly backup script for minecraft and trifling data

set -euo pipefail

MOUNT_POINT="${node.metadata['backups']['external_mount']}"
MINECRAFT_SOURCE="${node.metadata['backups']['minecraft_source']}"
TRIFLING_SOURCE="${node.metadata['backups']['trifling_source']}"
MINECRAFT_DEST="$MOUNT_POINT/backups/minecraft/survivalone"
TRIFLING_DEST="$MOUNT_POINT/backups/trifling"

# Generate timestamp in minecraft format: YYYY.MM.DD.HH.MM.SS
TIMESTAMP=$(date +%Y.%m.%d.%H.%M.%S)

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

cleanup() {
    if mountpoint -q "$MOUNT_POINT"; then
        log "Unmounting $MOUNT_POINT"
        umount "$MOUNT_POINT" || log "WARNING: Failed to unmount $MOUNT_POINT"
    fi
}

trap cleanup EXIT

log "Starting backup process"

# Mount the external disk
log "Mounting $MOUNT_POINT"
if ! mount "$MOUNT_POINT"; then
    log "ERROR: Failed to mount $MOUNT_POINT"
    exit 1
fi

# Create destination directories if they don't exist
mkdir -p "$MINECRAFT_DEST"
mkdir -p "$TRIFLING_DEST"

# Backup minecraft - copy the latest non-empty backup file
log "Backing up minecraft data"
LATEST_MINECRAFT=$(find "$MINECRAFT_SOURCE" -name "*.tar.gz" -type f -size +0 -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
if [ -n "$LATEST_MINECRAFT" ]; then
    BACKUP_NAME=$(basename "$LATEST_MINECRAFT")
    cp -v "$LATEST_MINECRAFT" "$MINECRAFT_DEST/$BACKUP_NAME"
    log "Minecraft backup complete: $BACKUP_NAME"
else
    log "WARNING: No non-empty minecraft backups found"
fi

# Backup trifling - create tar.gz of data directory
log "Backing up trifling data"
TRIFLING_BACKUP="$TRIFLING_DEST/$TIMESTAMP.tar.gz"
if [ -d "$TRIFLING_SOURCE" ]; then
    tar -czf "$TRIFLING_BACKUP" -C "$(dirname "$TRIFLING_SOURCE")" "$(basename "$TRIFLING_SOURCE")"
    log "Trifling backup complete: $(basename "$TRIFLING_BACKUP")"
else
    log "WARNING: Trifling source directory not found: $TRIFLING_SOURCE"
fi

log "Backup process complete"
