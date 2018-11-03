#!/bin/bash
# A backup Script for /Storage 

# Backup source
sourceloc='/Storage'

sendgridapikey='<Grab from Lastpass>'
sendgridurl='https://api.sendgrid.com/v3/mail/send'

# Exclusions
excl='--exclude=/Storage/.Trash-1000 --exclude=/Storage/Storage/Media/Film --exclude=/Storage/Storage/Media/Serier --exclude=/Storage/.backup --exclude=/Storage/Nextcloud_Data/*/uploads'

# Backup destination
dest='/Storage/.backup'

# Backup retention (in months)
retention='2'

# External Backup Location
bucket=gs://standersson-se-backup

# File containing previous backups
fullfile='/usr/local/backupscript/lastfullbackup'
diffile='/usr/local/backupscript/lastbackup'

# Log File
logfile='/var/log/bucketbackups'

# Today's Date
day=$(date +%y-%m-%d-%H-%M)


# Record Start time
starttime=$(date +%s)

function fullbackup {
	# Log start status message 
	echo "$(date +%y-%m-%d-%H-%M) - Full backup started" | tee -a $logfile

	# Run Backup job
	tar czf $dest/$archive_file $excl $sourceloc

	# Update the 'last full backup' file
	echo $(date +%y-%m-%d-%H-%M) > $fullfile
}

function diffbackup {
	# Log start status message 
	echo "$(date +%y-%m-%d-%H-%M) - Backup Started at: $(date +%R)" | tee -a $logfile

	# Run Backup job
	tar czf $dest/$archive_file $excl --newer $fullfile $sourceloc
}

if [ "$(date +%d)" = "01" ]; then
	# Name the archive
	archive_file="$day.tgz"
	fullbackup
else
	#Name the archive
	lastfull=$(cat $fullfile)
	archive_file="$day-diff-$lastfull.tgz"
	diffbackup
fi


#Log exit status
exittime=$((($(date +%s)-$starttime)/60))
hours=$(($exittime/60))
mins=$(($exittime-($hours*60)))
if [ "$hours" = "0" ]; then
	durat="$mins m"
else
	durat="$hours h $mins m"
fi
echo "$(date +%y-%m-%d-%H-%M) - Packaging Completed - it took $durat" | tee -a $logfile


# Copy backup to the external backup server

# Size of the file to be sent
lsize=$(ls -l $dest/$archive_file |cut -d" " -f5)

# Record Start time
transstart=$(date +%s)

#Code to set the timer

echo "Archive size: $lsize"

gsutil cp $dest/$archive_file gs://standersson-se-backup/
transfer_status=$?

#Log transfer time
transdone=$((($(date +%s)-$transstart)/60))
thours=$(($transdone/60))
tmins=$(($transdone-($thours*60)))
if [ "$thours" = "0" ]; then
	tdurat="$tmins m"
else
	tdurat="$thours h $mins m"
fi

if [ $transfer_status -eq 0 ]; then
	echo "$(date +%y-%m-%d-%H-%M) - Transfer Completed - it took $tdurat to send $(((lsize)/1000000)) MB" | tee -a $logfile
else
	echo "$(date +%y-%m-%d-%H-%M) - Transfer Failed - Failed after $tdurat. File was $(((lsize)/1000000)) MB" | tee -a $logfile

	curl --request POST --url $sendgridurl --header "Authorization: Bearer $sendgridapikey" --header 'Content-Type: application/json' --data '{"personalizations": [{"to": [{"email": "stefan.nigma@gmail.com"}]}],"from": {"email": "backup@standersson.se"},"subject": "Backup transmission failed","content": [{"type": "text/plain", "value": "Backup transfer to backup server failed!"}]}'
fi

# Remove old backups
if [ $transfer_status -eq 0 ]; then
	echo "$(date +%y-%m-%d-%H-%M) - Removing old backups" | tee -a $logfile
	oldbackups=$(gsutil ls gs://standersson-se-backup/ | grep -vi diff | head -n -$retention | cut -d"/" -f4)

	for item in $oldbackups
	do
		echo "$(date +%y-%m-%d-%H-%M) - Removing $item" | tee -a $logfile
		gsutil rm gs://standersson-se-backup/$item
	done
else
	echo "$(date +%y-%m-%d-%H-%M) - Backup failed, skipping old backup cleaning" | tee -a $logfile
fi