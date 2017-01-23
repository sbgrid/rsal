#!/usr/bin/env python

'''
mock api endpoint
'''

from flask import Flask, request
import json

app = Flask( __name__ )

@app.route('/dataverse_stub/published', methods=['POST'])
def dataverse_mock():
    '''
    stub so that the async release process has something to call
    '''
    print('dataverse_mock called')
    return 'dataverse_mock called'

@app.route('/release',methods=['POST'])
def release_dataset():
    '''
    recieve requests to release datasets.
    stored on filesystem for accessability to async release process
    '''
    dat = request.json
    dset_id = dat['datasetId']
    with open( 'data/%d.json' % dset_id, 'w' ) as opf:
        json.dump( dat, opf, indent = 2 )
    return 'ok'
    

if __name__ == '__main__':
    app.run()
