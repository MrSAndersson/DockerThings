#!/bin/bash

mv /home/minecraft/server.jar /home/minecraft/server/server.jar
exec /usr/bin/java -Xmx1024M -Xms1024M -jar server.jar nogui