#!/bin/bash

cd /home/minecraft/server

if [ -z "$(ls -A /home/minecraft/zip)" ]; then
   echo "Resuming Using the same FTB version"
else
    echo "New container, override FTB files"
    rm -rf config libraries modpack mods version.json FTBServer-*
    mv /home/minecraft/zip/* .
fi



./ServerStart.sh