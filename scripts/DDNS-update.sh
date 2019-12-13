#!/bin/sh

LAST="$(cat /tmp/DDNS.tmp)"
IP="$(dig +short myip.opendns.com @resolver1.opendns.com)"
if [ "$LAST" != "$IP" ]; then
	 RESPONSE="$(curl "https://dyn.dns.he.net/nic/update" -d "hostname=standersson.se" -d "password=<LASTPASS>" -k -d "myip=$IP")"
     RESPONSE="$(curl "https://dyn.dns.he.net/nic/update" -d "hostname=svard.me" -d "password=<LASTPASS>" -k -d "myip=$IP")"
     RESPONSE_IP=$(echo $RESPONSE | cut -d" " -f2)
	if [ "${RESPONSE_IP}" = "$IP" ]; then
		echo $IP > /tmp/DDNS.tmp
		echo "$(date): $RESPONSE_IP" >> /var/log/DDNS
    else
        echo "$(date): $RESPONSE" >> /var/log/DDNS
	fi
fi
