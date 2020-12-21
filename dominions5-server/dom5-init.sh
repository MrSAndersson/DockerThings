#!/bin/bash
./steamcmd/steamcmd.sh +login zappka +force_install_dir /home/steam/dom5 +app_update 722060 +quit

mkdir ~/.dominions5/mods ~/.dominions5/maps 

cd ~/.dominions5/maps
wget http://llamaserver.net/executor/Dominions%20Maps/FloatingArchipelago.zip 
unzip FloatingArchipelago.zip

cd ~/.dominions5/mods
cp ~/AI_No_RecruitV.6.zip .
unzip AI_No_RecruitV.6.zip
