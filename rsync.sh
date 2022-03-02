#!/bin/bash

set -e

docker pull $1
sleep 1
docker tag $1 $2
sleep 1
docker pull $2

exit 0