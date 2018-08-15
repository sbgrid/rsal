#!/bin/sh

# storage identifier for first file in a dataset

#dset=33
dset=$1

if [ -z "$dset" ]; then
	echo "dataset unspecified"
	exit
fi

h="http://localhost:8088"
#h="http://dvapp:8080"

#if [ -z "${ADMIN_KEY}" ]; then         
if [ -z "${key_dataverseAdmin}" ]; then         
	echo "source env_admin.sh or env.sh"  
	exit                                  
fi                                            
#k=${ADMIN_KEY}
k=${key_dataverseAdmin}

curl -s -X GET -H "X-Dataverse-key: $k" "${h}/api/datasets/:persistentId/?persistentId=doi:10.5072/FK2/${dset}" | jq -r '.data.latestVersion.files | .[0] | .dataFile.storageIdentifier'

