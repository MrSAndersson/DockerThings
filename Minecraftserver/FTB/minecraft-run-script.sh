#!/bin/bash
docker stop minecraft
docker rm minecraft
docker pull zappka/minecraft:latest
docker run --restart always -d -v minecraft:/home/minecraft/server -p 25564:25565 --name=minecraft zappka/minecraft:latest