#!/bin/bash

mv /home/minecraft/server.jar /home/minecraft/server/server.jar
exec java -Xmx1024M -Xms1024M -jar server.jar nogui
