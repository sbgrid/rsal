#!/bin/sh

# mock for waiting; actually doing stuff, and then telling dv to continue
logfile=pub.out

# DVAPIKEY IN BASHRC
source ${HOME}/.bashrc

# change this to the dataverse host
h=dvapp:8080
invk_id=$1
dset=$2

echo "starting at `date`" >> $logfile


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
sid=`curl -s -X GET -H "X-Dataverse-key: $DVAPIKEY" "${h}/api/datasets/:persistentId/?persistentId=doi:10.5072/FK2/${dset}" | jq -r '.data.latestVersion.files | .[0] | .dataFile.storageIdentifier'`


echo $sid >> $logfile



#echo "storage identifier $sid for dataset $dset " >> $logfile
#echo "start moving data" >> $logfile
#cp -r -p /hold/${dset}/${sid} //public/FK2/${dset}
#echo "done moving data" >> $logfile
echo "pretending rsal is doing stuff by sleeping for 30s" >> $logfile
sleep 30
echo "done pretending, tell dv we're done" >> $logfile

curl -i -X POST -H "Content-Type: text/plain" -H "X-Dataverse-key: ${DVAPIKEY}" ${h}/api/workflows/${invk_id} -d "OK" >> $logfile

echo "all done" >> $logfile
