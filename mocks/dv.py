#!/usr/bin/env python

'''
mock dataverse API endpoint for RSAL development
'''

from flask import Flask

app = Flask( __name__ )

@app.route('/storage_query/<x>',methods=['GET'])
def storage_id_query(x):
    return 'storage id would go here\n'

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

