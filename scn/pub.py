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
import glob

def storage_id_query_mock(dv_api_key, dv_host, dset_pid): 
    return '16389c3b4de-8052ecdd77c1'

def storage_id_query(dv_api_key, dv_host, dset_pid):
    #return storage_id_query_mock(dv_api_key,dv_host,dset_pid)
    u = '%s/api/datasets/:persistentId/' % dv_host
    print(u)
    r = requests.get(u, params={'persistentId':dset_pid},headers={'X-Dataverse-key':dv_api_key})
    if 200 == r.status_code:
        j = r.json()
        fs = j['data']['latestVersion']['files']
        if 1 != len(fs):
            sys.stderr.write('ERROR: unexpected number of files reported for datataset %s\n'%(dset_pid))
            sys.exit(1)
        sid=fs[0]['dataFile']['storageIdentifier']
        return sid
    else:
        sys.stderr.write('ERROR: %d response from dataverse storage id query for %s\n' %(r.status_code, dset_pid))
        sys.exit(1)

def resume_workflow(dv_api_key, dv_host, invk_id):
    u = '%s/api/workflows/%s' % ( dv_host, invk_id )
    r = requests.post(u, data='OK',headers={'X-Dataverse-key':dv_api_key})
    if 202 != r.status_code:
        sys.stderr.write('ERROR: problem resuming workflow %s (dataverse said %d)\n'%(invk_id,r.status_code))
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
            sys.stderr.write('ERROR - unable to retrieve %s environment variable\n')
            sys.exit(1)
    return r

def pub(rfile, src=None, cfg=None):
    sys.stdout.write('publishing from request file %s\n'%rfile)
    with open(rfile,'r') as inp:
        x = json.load( inp )
    invk_id = x['invocationId']
    ident = x['datasetIdentifier']
    pid = x['datasetPersistentIdentifier']
    sys.stdout.write('PID %s : invocation %s\n'%(pid,invk_id))
    if None == cfg:
        cfg = get_env_config()
    sid = storage_id_query( cfg['DV_API_KEY'],cfg['DV_HOST'], pid ) # dataverse API query since storage id isn't available in workflow invocation
    sys.stdout.write('storage ID: %s\n'%sid)
    src = os.path.join(HOLD,ident,sid)
    # sync/copy
    dst = os.path.join( PUBLIC, DOISHOULDER, x['datasetIdentifier'] )
    shutil.copytree( src, dst )

    # verify (optional TODO)

    # clean / symlink
    shutil.rmtree( src )
    os.symlink( dst, src )

    # report to dataverse that workflow can resume (TODO)
    sys.stdout.write('telling DV to resume\n')
    resume_workflow(cfg['DV_API_KEY'],cfg['DV_HOST'],invk_id)
    sys.stdout.write('done\n')

def pub_avail():
    rs = glob.glob('%s/*.json'%(REQDIR))
    for r in rs:
        print(r)
        pub(r)

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

def test3():
    pub_avail()

if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    pub_avail()

