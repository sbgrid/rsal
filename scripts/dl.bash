#!/usr/bin/env bash

h=rsync://localhost
ds_ident=1QKK1K
pid=10.5072/FK2/${ds_ident}

if [ ! -d tmp/ ]; 
then
	mkdir tmp/
fi
cd tmp/
if [ -d ${ds_ident} ];
then
	echo "cleaning up from previous run"
	rm -r ${ds_ident}
fi
echo ${h}/${pid}
rsync -av ${h}/${pid} .
cd ${ds_ident}
if [ ! -e files.sha ];
then
	echo "error - failed to download manifest (possibly other files)"
	exit 1
fi
shasum -c files.sha
#cd ../../

