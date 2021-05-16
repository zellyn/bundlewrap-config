# bundlepi
[bundlewrap.org](https://bundlewrap.org) config for my raspberry pis.

This is Zellyn's bundlewrap configuration for his Raspberry Pis. Feel free to use any or all of it if it useful to you. It is likely to be of varying quality, as I am new to bundlewrap.

I have four Raspberry Pi 4s for a Kubernetes cluster, bought with a work-provided educational allowance. I also have a personal Raspberry Pi 4, and a Pi Zero W. I manage all through bundlewrap: the division should be clear in `groups.py`.

The notes we're taking as we configure Raspberry Pi Kubernetes clusters are [here](https://docs.google.com/document/d/12TT49VgyPRSH7F4b_oC5rOv1Ag7RPxmSNAWbJjf3RF4).

# Miscellaneous notes

### Dumping file contents and other general debugging
```
bw items katespi1
bw items -f katespi1 file:/etc/keepalived/keepalived.conf
bw items -f katespi1 file:/etc/systemd/system/k3s.service
bw debug -c 'print(repo.vault.password_for("foobarbaz"))'
```
