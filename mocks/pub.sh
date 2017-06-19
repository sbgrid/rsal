#!/bin/sh

# mock for waiting; actually doing stuff, and then telling dv to continue
logfile=pub.out

h=dvapp:8080
invk_id=$1
dset=$2

echo "starting at `date`" >> $logfile
key_dataverseAdmin="0bb4f38b-04c7-4405-929d-57d64bfb1811"
if [ -z "${key_dataverseAdmin}" ]; then
	. env_admin.sh
fi
echo "key ok" >> $logfile

if [ -z "${invk_id}" ]; then
	echo "no invokation id specified; bailing out"
	exit 1
fi

if [ -z "${dset}" ]; then
	echo "no dataset specified; bailing out"
	exit 1
fi

echo "invokation id ok" >> $logfile

# now actually doing work

# need to get storage identifier
sid=`curl -s -X GET -H "X-Dataverse-key: $k" "${h}/api/datasets/:persistentId/?persistentId=doi:10.5072/FK2/${dset}" | jq -r '.data.latestVersion.files | .[0] | .dataFile.storageIdentifier'`
#sid0=`curl -s -X GET -H "X-Dataverse-key: $k" "${h}/api/datasets/:persistentId/?persistentId=doi:10.5072/FK2/${dset}" `
#sid0=`curl  -X GET -H "X-Dataverse-key: $k" "${h}/api/datasets/:persistentId/?persistentId=doi:10.5072/FK2/${dset}" `
echo $sid
#exit
#echo "sleeping for 60s" >> $logfile
echo "storage identifier $sid for dataset $dset " >> $logfile
echo "start moving data" >> $logfile
cp -r -p /hold/${dset}/${sid} //public/FK2/${dset}
echo "done moving data" >> $logfile

#echo "woke up; telling DV we're done" >> $logfile

curl -i -X POST -H "Content-Type: text/plain" -H "X-Dataverse-key: ${ADMIN_KEY}" ${h}/api/workflows/${invk_id} -d "OK"

echo "all done" >> $logfile
