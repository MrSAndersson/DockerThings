#!/bin/bash
docker pull zappka/minecraft-bedrock:latest
docker stop bedrock
docker rm bedrock
docker run --restart always -d -v bedrock:/home/minecraft/worlds -p 19132:19132/udp --name=bedrock zappka/minecraft-bedrock:latest
