#!/usr/bin/env bash

# "act like dataverse" calling RSAL to request publication"

h=http://localhost:8889
#h=http://localhost

pid=$$

dsid=3
#dsident=1
dsident=1QKK1K
stid=16389c3b4de-8052ecdd77c1
d_pid="doi:10.5072/FK2/1QKK1K"
invid="InvokeMe"

TMPFILE=/tmp/${pid}.txt
echo $invid > $TMPFILE
echo "dataset.id=$dsid" >> $TMPFILE
echo "dataset.identifier=$dsident" >> $TMPFILE
#echo "dataset.storageid_package=${stid}" >> $TMPFILE
echo "dataset.globalId=${d_pid}" >> $TMPFILE

curl -i -X POST --data-binary @$TMPFILE ${h}/rr.py

