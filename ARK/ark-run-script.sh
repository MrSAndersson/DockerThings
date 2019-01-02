#!/bin/bash
docker stop ark
docker rm ark
docker pull zappka/ark:latest
docker run --restart always -d -v ark:/home/steam/ark \
    -p 7777:7777/udp \
    -p 7778:7778/udp \
    -p 27015:27015/udp \
    -p 27020:27020/tcp \
    -e SESSION_NAME=<YOUR SESSION NAME> \
    -e SERVER_PASS=<YOUR SERVER PASS> \
    -e ADMIN_PASS=<YOUR ADMIN PASS> \
    --name=ark zappka/ark:latest