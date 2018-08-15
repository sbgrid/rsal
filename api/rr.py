#!/usr/bin/env python

'''
release request reciever
'''

REQDIR='/public/stage/'

import sys
import os
import json

def recieve():
    print('Content-type: text/plain\n')
    txt = sys.stdin.read()
    # currently getting text from dataverse workflow
    lns = txt.splitlines()
    def get_key(k):
        ys = [ ln for ln in lns if ln.startswith('%s='%k) ]
        assert( 1 == len(ys) )
        z = ys[0].split()[0]
        p = z.find('=')
        assert( -1 != p )
        return z[p+1:]
    inv_id = lns[0].strip()
    def get_identifier( xs ):
        ys = [ ln for ln in lns if ln.startswith('dataset.identifier=') ]
        assert( 1 == len(ys) )
        z = ys[0].split()[0]
        p = z.find('=')
        assert( -1 != p )
        return z[p+1:].strip()
    try:
        #did = get_identifier( lns )
        did = get_key( 'dataset.identifier')
        #sid = get_key('dataset.storageid_package') 
        dbid = get_key('dataset.id')
        d_pid = get_key('dataset.globalId')
        pid = os.getpid()
        #xs = {'datasetIdentifier':did, 'invocationId':inv_id,'storageId':sid,'dbId':dbid}
        xs = {'datasetIdentifier':did, 'invocationId':inv_id,'dbId':dbid,'datasetPersistentIdentifier':d_pid}
        fn = os.path.join( REQDIR, '%d.json' % pid )
        with open(fn, 'w') as opf:
            #opf.write(txt)
            opf.write( json.dumps( xs ) )
        print('Status: 200 OK\n\nOK')
    except AssertionError:
        print('Status: 400 Bad Request\n\nfailed assert\n')
    except IOError:
        print('Status: 500 Internal Server Error\n\nIO issue\n')

if __name__ == '__main__':
    recieve()
