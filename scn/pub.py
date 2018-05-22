#!/usr/bin/env python

REQDIR='.'
DOISHOULDER='10.5072/FK2'
HOLD='/hold'
PUBLIC='/public'

import json
import requests
import sys
import shutil
import os.path
import os

def pub(rfile, src=None):
    with open(rfile,'r') as inp:
        x = json.load( inp )
    # get storage identifier for DV package file from dataverse
    if None == src:
        print('storage id query unimplemented')
        sys.exit(1)
    # sync/copy
    dst = os.path.join( PUBLIC, DOISHOULDER, x['datasetIdentifier'] )
    shutil.copytree( src, dst )

    # verify (TODO)

    # clean / symlink
    shutil.rmtree( src )
    os.symlink( dst, src )
