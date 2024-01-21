#!/usr/bin/env bash
set -euo pipefail

bw run all -p 100 "apt-get update && apt-get -y upgrade && apt -y autoremove"
