#! /usr/bin/env bash
SS_DIR=$(dirname $(realpath $0))
cd $SS_DIR/..
GOOS=linux GOARCH=arm64 go build -o simpleserver/bin/simpleserver ./simpleserver/
cd $SS_DIR
docker build -t simpleserver .
docker image tag simpleserver:latest zellyn/katespi:simpleserver-latest

if [[ ${1:-} == 'push' ]]; then
    docker push zellyn/katespi:simpleserver-latest
fi