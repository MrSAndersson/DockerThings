#!/bin/bash

if [[ ! -v SESSION_NAME ]]; then
    export SESSION_NAME="ARK-Server"
fi

if [[ ! -v SERVER_PASS ]]; then
    export SERVER_PASS=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c15)
fi

if [[ ! -v ADMIN_PASS ]]; then
    export ADMIN_PASS=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c15)
fi

cd /home/steam/steamcmd

./steamcmd.sh +login anonymous +force_install_dir /home/steam/ark +app_update 376030 +quit

cd /home/steam/ark/ShooterGame/Binaries/Linux
./ShooterGameServer TheIsland?listen?SessionName=${SESSION_NAME}?ServerPassword=${SERVER_PASS}?ServerAdminPassword=${ADMIN_PASS} -server -log