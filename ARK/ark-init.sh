#!/bin/bash

if [[ ! -v SESSION_NAME ]]; then
    export SESSION_NAME="ARK-Server"
fi

if [[ ! -v SERVER_PASS ]]; then
    export SERVER_PASS=''
fi


cd /home/steam/steamcmd

./steamcmd.sh +login anonymous +force_install_dir /home/steam/ark +app_update 376030 +quit

cd /home/steam/ark/ShooterGame/Binaries/Linux


if [[ -v ARK_OPTIONS ]]; then
    ./ShooterGameServer TheIsland?listen?SessionName=${SESSION_NAME}?ServerPassword=${SERVER_PASS}?${ARK_OPTIONS} -server -log
else
    ./ShooterGameServer TheIsland?listen?SessionName=${SESSION_NAME}?ServerPassword=${SERVER_PASS} -server -log
fi