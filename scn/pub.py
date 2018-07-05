#!/usr/bin/env python

REQDIR='.'
#DOISHOULDER='10.5072/FK2'
DOISHOULDER='FK2'
HOLD='/hold'
PUBLIC='/public'

import json
#import requests
import sys
import shutil
import os.path
import os

def storage_id_query(dv_api_key, dv_host, dset_pid): #TODO - stub
    return '16389c3b4de-8052ecdd77c1'


def pub(rfile, src=None):
    with open(rfile,'r') as inp:
        x = json.load( inp )
    ident = x['datasetIdentifier']
    pid = x['datasetPersistentIdentifier']
    #sid = x['storageId'] #FIXME - storage id not available in workflow invocations; query dataverse API instead
    sid = storage_id_query(None, None, pid )
    invk_id = x['invocationId']
    src = os.path.join(HOLD,ident,sid)
    # sync/copy
    dst = os.path.join( PUBLIC, DOISHOULDER, x['datasetIdentifier'] )
    shutil.copytree( src, dst )

    # verify (TODO)

    # clean / symlink
    shutil.rmtree( src )
    os.symlink( dst, src )

    # report to dataverse that workflow can resume (TODO)

if __name__ == '__main__':
    try:
        rf = sys.argv[1]
    except IndexError:
        print('testing - pub.py [request file]')
        sys.exit(1)
    pub(rf)
