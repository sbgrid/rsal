#!/usr/bin/env python

REQDIR='/public/stage'
REQPUB='/public/requests'
#DOISHOULDER='10.5072/FK2'
DOISHOULDER='FK2'
HOLD='/hold'
PUBLIC='/public'

import json
import requests
import sys
import shutil
import os.path
import os

def storage_id_query_mock(dv_api_key, dv_host, dset_pid): 
    return '16389c3b4de-8052ecdd77c1'

def storage_id_query(dv_api_key, dv_host, dset_pid):
    #return storage_id_query_mock(dv_api_key,dv_host,dset_pid)
    u = '%s/api/datasets/:persistentId/' % dv_host
    r = requests.get(u, params={'persistentId':dset_pid},headers={'X-Dataverse-key':dv_api_key})
    if 200 != r.status_code:
        j = r.json()
        fs = j['data']['latestVersion']['files']
        if 1 != len(fs):
            sys.stderr.write('ERROR: unexpected number of files reported for datataset %s'%(dset_pid))
            sys.exit(1)
        sid=fs[0]['dataFile']['storageIdentifier']
        return sid
    else:
        sys.stderr.write('ERROR: %d response from dataverse storage id query for %s' %(r.status_code, dset_pid))
        sys.exit(1)

def get_env_config():
    '''
    retrieve config info from environmental variables.
    DV_API_KEY, DV_HOST to start with
    '''
    r = {}
    ks = ['DV_API_KEY','DV_HOST']
    for k in ks:
        try:
            v = os.environ[k]
            r[k] = v
        except KeyError:
            sys.stderr.write('ERROR - unable to retrieve %s environment variable')
            sys.exit(1)
    return r

def pub(rfile, src=None, cfg=None):
    with open(rfile,'r') as inp:
        x = json.load( inp )
    ident = x['datasetIdentifier']
    pid = x['datasetPersistentIdentifier']
    if None == cfg:
        cfg = get_env_config()
    sid = storage_id_query( cfg['DV_API_KEY'],cfg['DV_HOST'], pid ) # dataverse API query since storage id isn't available in workflow invocation
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

def test1():
    try:
        rf = sys.argv[1]
    except IndexError:
        print('testing - pub.py [request file]')
        sys.exit(1)
    pub(rf)

def test2():
    r = get_env_config()
    print(r)

if __name__ == '__main__':
    #test1()
    test2()

