#!/usr/bin/env bash

# Copied from https://get.k3s.io/, with some simplifications.

# INSTALL_K3S_CHANNEL=stable
INSTALL_K3S_CHANNEL=latest

GITHUB_URL=https://github.com/k3s-io/k3s/releases
SUFFIX=-arm64
INSTALL_K3S_CHANNEL_URL=https://update.k3s.io/v1-release/channels
version_url="${INSTALL_K3S_CHANNEL_URL}/${INSTALL_K3S_CHANNEL}"
VERSION_K3S=$(curl -w '%{url_effective}' -L -s -S ${version_url} -o /dev/null | sed -e 's|.*/||')
BIN_URL=${GITHUB_URL}/download/${VERSION_K3S}/k3s${SUFFIX}
echo "Downloading $BIN_URL"
curl -o bin/k3s${SUFFIX} -sfL $BIN_URL
# wget -qO bin/k3s${SUFFIX} $BIN_URL
