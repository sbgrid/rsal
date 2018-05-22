#!/usr/bin/env python

'''
release request reciever
'''
#
REQDIR='/public/stage/'

import sys
import os

def recieve():
    print('Content-type: text/plain\n')
    txt = sys.stdin.read()
    # currently getting text from dataverse workflow
    lns = txt.splitlines()
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
        pid = os.getpid()
        xs = {'datasetIdentifier':did, 'invocationId':inv_id}
        fn = os.path.join( REQDIR, '%d.json' % pid )
        with open(fn, 'w') as opf:
            opf.write(txt)
        print('Status: 200 OK\n\nOK')
    except AssertionError:
        print('Status: 400 Bad Request\n\nfailed assert\n')
    except IOError:
        print('Status: 500 Internal Server Error\n\nIO issue\n')

if __name__ == '__main__':
    recieve()
