#!/bin/sh

# mock for waiting; actually doing stuff, and then telling dv to continue
logfile=Resume.out

echo "starting at `date`" >> $logfile

if [ -z "${ADMIN_KEY}" ]; then
	. env_admin.sh
fi
echo "key ok" >> $logfile

invk_id=$1
if [ -z "${invk_id}" ]; then
	echo "no invokation id specified; bailing out"
	exit 1
fi
echo "invokation id ok" >> $logfile

echo "sleeping for 60s" >> $logfile
sleep 60

h=dvapp:8080

echo "woke up; telling DV we're done" >> $logfile

curl -i -X POST -H "Content-Type: text/plain" -H "X-Dataverse-key: ${ADMIN_KEY}" ${h}/api/workflows/${invk_id} -d "OK"

echo "all done" >> $logfile
