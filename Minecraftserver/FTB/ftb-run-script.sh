#!/bin/bash
docker stop ftb
docker rm ftb
docker pull zappka/ftb:latest
docker run --restart always -d -v ftb:/home/minecraft/server -p 25565:25565 --name=ftb zappka/ftb:latest