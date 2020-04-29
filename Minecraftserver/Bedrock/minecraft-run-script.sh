#!/bin/bash
docker stop bedrock
docker rm bedrock
docker pull zappka/minecraft-bedrock:latest
docker run --restart always -d -v bedrock:/home/minecraft/worlds -p 19132:19132 -p 35109:35109 --name=bedrock zappka/minecraft-bedrock:latest
