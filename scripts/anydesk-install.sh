#!/bin/bash

cp anydesk /usr/bin/
chmod 755 /usr/bin/anydesk

cp anydesk.desktop /usr/share/applications/
chmod 644 /usr/share/applications/anydesk.desktop

mkdir /usr/share/doc/anydesk
cp {copyright,README} /usr/share/doc/anydesk/
chmod 644 /usr/share/doc/anydesk/{copyright,README}

cp -R icons /usr/share/
find /usr/share/icons/hicolor/ -name "anydesk.*" -exec chmod 644 {} \;

cp polkit-1/com.philandro.anydesk.policy /usr/share/polkit-1/rules.d/
chmod 644 /usr/share/polkit-1/rules.d/com.philandro.anydesk.policy

cp systemd/anydesk.service /etc/systemd/system/
chmod 755 /etc/systemd/system/anydesk.service