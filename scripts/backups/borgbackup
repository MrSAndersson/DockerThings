#!/bin/bash

logfile='/var/log/backups'

# Sendgrid variables
sendgridapikey='<LastPass>'
sendgridurl='https://api.sendgrid.com/v3/mail/send'
notifyaddress='<email-address>'


echo "Starting Backup"
echo "$(date "+%m-%d %H:%M") - Cloud Backup Started" >> $logfile


# Backup  
erroroutput="$(borg create --exclude '/Storage/Nextcloud_Data/*/uploads' --exclude '/Storage/.Trash-1000' --exclude '/Storage/Storage/Media/Film' --exclude '/Storage/Storage/Media/Serier' --stats borg@cloud.standersson.se:storage::Storage-$(date +%y-%m-%d) /Storage 2>&1 > /dev/null)"

backup_exit=$?

case ${backup_exit} in
0)
    echo "Backup finished successfully"
 	echo "$(date "+%m-%d %H:%M") - Cloud Backup finished successfully" >> $logfile
;;
1)
    #Backup Warning
    echo "Backup finished with a warning"
    echo "$(date "+%m-%d %H:%M") - Cloud Backup finished with a warning" >> $logfile
    curl --request POST --url $sendgridurl --header "Authorization: Bearer $sendgridapikey" --header 'Content-Type: application/json' \
        --data '{"personalizations": [{"to": [{"email": "'$notifyaddress'"}]}],"from": {"email": "backup@standersson.se"},"subject": "Standersson Backup Warning","content": [{"type": "text/plain", "value": "$erroroutput"}]}'
;;
*)    
    #Backup Error
    echo "Backup finished with an error"
    echo "$(date "+%m-%d %H:%M") - Cloud Backup finished with an error" >> $logfile
    curl --request POST --url $sendgridurl --header "Authorization: Bearer $sendgridapikey" --header 'Content-Type: application/json' \
        --data '{"personalizations": [{"to": [{"email": "'$notifyaddress'"}]}],"from": {"email": "backup@standersson.se"},"subject": "Standersson Backup Error","content": [{"type": "text/plain", "value": "$erroroutput"}]}'
;;
esac

if [ ${backup_exit} -eq 0 ]; then

    echo "Pruning repository"

    pruneerroroutput="$(borg prune --list --show-rc --keep-daily 7 --keep-weekly 4 --keep-monthly 6 borg@cloud.standersson.se:storage 2>&1 > /dev/null)"

    prune_exit=$?

    case ${prune_exit} in
    0)
        echo "Pruning finished successfully"
    	echo "$(date "+%m-%d %H:%M") - Cloud Pruning finished successfully" >> $logfile
    ;;
    1)
        echo "Pruning finished with a warning"
        echo "$(date "+%m-%d %H:%M") - Cloud Pruning finished with a warning" >> $logfile
        curl --request POST --url $sendgridurl --header "Authorization: Bearer $sendgridapikey" --header 'Content-Type: application/json' \
	        --data '{"personalizations": [{"to": [{"email": "'$notifyaddress'"}]}],"from": {"email": "backup@standersson.se"},"subject": "Standersson Pruning Warning","content": [{"type": "text/plain", "value": "$pruneerroroutput"}]}'
    ;;
    *)
        echo "Pruning finished with an error"
        echo "$(date "+%m-%d %H:%M") - Cloud Pruning finished with an error" >> $logfile
        curl --request POST --url $sendgridurl --header "Authorization: Bearer $sendgridapikey" --header 'Content-Type: application/json' \
	        --data '{"personalizations": [{"to": [{"email": "'$notifyaddress'"}]}],"from": {"email": "backup@standersson.se"},"subject": "Standersson Pruning Error","content": [{"type": "text/plain", "value": "$pruneerroroutput"}]}'
    ;;
    esac
fi
