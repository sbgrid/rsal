#!/usr/bin/env python

import requests
import glob
import os
import json

dv_endpoint = 'http://localhost:8080/dataverse_stub/published'

def release_all( data_dir = 'data' ):
    for fn in glob.glob('%s/*.json' % data_dir ):
        with open(fn,'r') as inp:
            x = json.load( inp )
            dataset_release( x['datasetId'] )
        os.remove( fn )


def dataset_release( dset_id ):
    print('releasing %s ' % dset_id )
    r = requests.post( dv_endpoint, data = {'datasetId':dset_id} )
    print( r.text )

if __name__ == '__main__':
    release_all()

