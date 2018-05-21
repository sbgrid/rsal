#!/usr/bin/env python

'''
release request reciever
'''

REQDIR='/public/stage/'

import sys
import os

def recieve():
    txt = sys.stdin.read()
    def ok():
        print('Status: 200 OK\n\nOK')
        return
    def bad():
        print('Status: 400 Bad Request\n\n')
        return
    # currently getting text from dataverse workflow
    lns = txt.split('\n')
    inv_id = lns[0].strip()
    def get_identifier( xs ):
        ys = [ ln for ln in lns if ln.startswith('dataset.identifier=') ]
        assert( 1 == len(ys) )
        z = ys[0].split()[0]
        p = z.find('=')
        assert( -1 != p )
        return z[p+1:]
    try:
        did = get_identifier( lns )
    except AssertionError:
        bad()
    pid = os.getpid()
    xs = {'datasetIdentifier':did, 'invocationId':inv_id}
    fn = os.path.join( REQDIR, '%d.json' % pid )
    with open(fn, 'w') as opf:
        opf.write(txt)
    ok()

