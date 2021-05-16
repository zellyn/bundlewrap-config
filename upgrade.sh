#!/usr/bin/env bash
bw run all -p 100 "apt-get update && apt-get -y upgrade && apt -y autoremove"
