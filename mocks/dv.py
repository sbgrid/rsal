#!/usr/bin/env python

'''
mock dataverse API endpoint for RSAL development
'''

from flask import Flask,request,Response
import json

app = Flask( __name__ )

#@app.route('/storage_query/<x>',methods=['GET'])
#@app.route('/api/datasets/:persistentId/<x>',methods=['GET'])
#def storage_id_query(x):
@app.route('/api/datasets/:persistentId/',methods=['GET'])
def storage_id_query():
    x = request.args.get('persistentId')
    r = {'x':x,'data':{'latestVersion':{'files':[{'dataFile':{'storageIdentifier':'16389c3b4de-8052ecdd77c1'}}]}}}
    #return 'storage id would go here\n'
    #return json.dumps(r)
    return Response( json.dumps(r), mimetype='application/json')

@app.route('/resume/<x>', methods=['POST'])
def resume_workflow(x):
    return 'workflow %s resumed\n' % x

@app.route('/abort/<x>', methods=['POST'])
def abort_workflow(x):
    return 'workflow %s aborted\n' % x

@app.route('/')
def hello():
    return 'Dataverse API mock exists\n'

if __name__ == '__main__':
    app.run()

