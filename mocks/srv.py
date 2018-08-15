#!/usr/bin/env python

'''
mock api endpoint for a server that processes datasets prior
to them being released.

Start a release by POSTing to /release/. Format:
{
    id:<id>,
    name:<name>
}
'''

from flask import Flask, request, json, Response
import requests
import subprocess

app = Flask( __name__ )

datasets_in_release = {}

#@app.route('/dump/<v>', methods=['POST', 'DELETE'])
def dump_equest(v):
    '''
    Just dump the request you got to stdout.
    '''
    print("Got a %s request" % request.method )
    print("headers:")
    print(request.headers)
    print("/headers:")
    print("body:")
    print(request.data)
    print("/body")
    return ("OK")

#@app.route('/dump/<v>', methods=['POST', 'DELETE'])
@app.route('/release/<v>', methods=['POST', 'DELETE'])
def v2(v):
    body = request.data
    print('recieved body:')
    print(body)
    lns=body.split('\n')
    inv_id = lns[0].strip()
    print('invokation id: %s ' % inv_id )
    # we need the dataset identifier to get the storage identifier
    def get_identifier( xs ):
        ys = [ ln for ln in lns if ln.startswith('dataset.identifier=') ]
        assert( 1 == len(ys) )
        z = ys[0].split()[0]
        p = z.find('=')
        assert( -1 != p )
        #return int( z[p+1:] )
        return z[p+1:]
    did = get_identifier( lns )
    print('using %s as dataset identifier' % did )
    #print('calling subprocess')
    
    subprocess.Popen( ['./pub.sh',inv_id, str(did)] ) # claims env_admin.sh not found; but manages to successfull resume the workflow after sleep regardless.
    print('done')
    
    return ('OK')

@app.route('/start/', methods=['POST'])
def dataverse_mock():
    '''
    stub so that the async release process has something to call
    '''
    print("Got POST:")
    print(request.data)
    print("---")
    release_data = json.loads(request.data)
    print('started release process of %s' % release_data )
    print('id %s' % release_data[u'id'] )
    datasets_in_release[int(release_data[u'id'])] = release_data
    return '%s release started' % release_data[u'id']

@app.route('/pending/',methods=['GET'])
def list_pending():
    '''
    see what releases are pending
    '''
    return ("%s" % datasets_in_release.keys())

@app.route('/complete/<int:id>', methods=['POST'])
def release(id):
    '''
    tell dataverse that a given dataset release was completed, and so the DS
    release process can proceed.
    '''
    if ( datasets_in_release.has_key(id) ):
        print("process of dataset %s completed. Telling dataverse about that." % id)
        ds = datasets_in_release.pop(id)
        # TODO: POST ds to dataverse.
        return "Dataset %s released." % id
    else:
        return Response(response="Dataset %s not found." % id, status=404)


if __name__ == '__main__':
    app.run()
