#!/usr/bin/env bash

h=http://localhost:8889
#h=http://localhost

pid=$$

dsid=3
dsident=1
invid="InvokeMe"

TMPFILE=/tmp/${pid}.txt
echo $invid > $TMPFILE
echo "dataset.id=$dsid" >> $TMPFILE
echo "dataset.identifier=$dsident" >> $TMPFILE

curl -i -X POST --data-binary @$TMPFILE ${h}/rr.py

