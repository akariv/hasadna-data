import os
import json
import time
import httplib, urllib

DBSERVER = "127.0.0.1:5555"

class DBLoader(object):

    @staticmethod
    def del_collection(relpath):
        body = None
        headers = {"Content-type": "application/json",
                   "Accept": "application/json"}
        conn = httplib.HTTPConnection(DBSERVER)
        conn.request("DELETE", "%s/?apikey=admin" % (relpath,), body, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print data
        conn.close()        

    @staticmethod
    def new_item(relpath,slug,record):      
        body = json.dumps(record)
        headers = {"Content-type": "application/json",
                   "Accept": "application/json"}
        conn = httplib.HTTPConnection(DBSERVER)
        conn.request("POST", "%s/%s?apikey=admin" % (relpath,slug), body, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print data
        conn.close()        
