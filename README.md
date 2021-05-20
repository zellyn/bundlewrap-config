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

## Accessing your cluster with kubectl

Copy the cluster, context, and user from `/etc/rancher/k3s/k3s.yaml` on the
control-plane server into the relevant sections of `~/.kube/config`, renaming
`default` to `katespi` (or whatever you want) everywhere.

## How my cluster is set up with keepalived, etc.

# Notes as I go

- simpleserver/build.sh will build a hello-world http server on port 8080 for arm64, putting it in bin/simpleserver
- how to build an arm64 docker image?
  - build it `FROM scratch`… why not - it doesn't do anything yet, and we can
    use the [golang-docker-scratch
    recipe](https://github.com/jeremyhuiskamp/golang-docker-scratch) later if we
    need tzdata.
- how to let the k8s cluster find it?
  - use docker hub for now:

    ```
    docker build -t simpleserver .
    docker image tag simpleserver:latest zellyn/katespi:simpleserver-latest
    docker push zellyn/katespi:simpleserver-latest
    ```
  - maybe set up a private registry on the cluster in the future?

