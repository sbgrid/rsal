#!/usr/bin/env python

REQDIR='.'
DOISHOULDER='10.5072/FK2'
HOLD='/hold'
PUBLIC='/public'

import json
#import requests
import sys
import shutil
import os.path
import os

def pub(rfile, src=None):
    with open(rfile,'r') as inp:
        x = json.load( inp )
    ident = x['datasetIdentifier']
    sid = x['storageId']
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
