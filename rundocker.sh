#!/bin/bash

docker build -t amulet-editor .

xhost +local:docker

docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  --device /dev/dri \
  --network=host \
  amulet-editor

xhost -local:docker
