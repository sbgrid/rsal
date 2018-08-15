#!/usr/bin/env python

'''
mock dataverse API endpoint for RSAL development
'''

from flask import Flask,request,Response
import json

app = Flask( __name__ )

@app.route('/api/datasets/:persistentId/',methods=['GET'])
def storage_id_query():
    x = request.args.get('persistentId')
    r = {'x':x,'data':{'latestVersion':{'files':[{'dataFile':{'storageIdentifier':'16389c3b4de-8052ecdd77c1'}}]}}}
    return Response( json.dumps(r), mimetype='application/json')

@app.route('/api/workflows/<x>', methods=['POST'])
def resume_workflow(x):
    try:
        dv_key = request.headers['X-Dataverse-key']
        return 'workflow %s resumed\n' % x
    except KeyError:
        return 'unauthenticated for workflow %s resume'%x, 401

@app.route('/dump/<x>', methods=['POST'])
def abort_workflow(x):
    return 'workflow %s aborted\n' % x

@app.route('/')
def hello():
    return 'Dataverse API mock exists\n'

@app.route('/api/info/version')
def version():
    return '{"status":"OK","data":{"version":"4.8.1","build":"mock-for-rsal"}}'

if __name__ == '__main__':
    app.run()

