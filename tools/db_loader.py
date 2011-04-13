import os
import json
from field_loaders import FieldLoader

DBSERVER = "127.0.0.1:5555"


class DBLoader(object):

    def __init__(self,path,field_types):
        self.path = path
        self.field_types = field_types
        self.field_loader = FieldLoader(field_types)

    def del_collection(self):
        #### TODO - change to use a python library
        cmd = 'lwp-request -m DELETE %s%s/' % (DBSERVER, self.path, )
        print cmd
        _,_=os.popen2(cmd)

    def new_item(self,row):
        rec = {}
        for k, v in row.iteritems():
            d = rec
            parts = k.split('.')
            for part in parts[:-1]:
                d = rec.setdefault(part,{})
            d[parts[-1]] = self.field_loader.load_field(k,v) 
        
        slug = self.field_loader.extract_slug(rec)
        
        #### TODO - change to use a python library
        #print "Loading --> %s, %s :: %r" % (self.path, slug, rec)
        cmd = 'lwp-request -c application/json -m POST %s%s/%s' % (DBSERVER, self.path, slug, )
        print cmd
        i,_=os.popen2(cmd)
        i.write(json.dumps(rec))
        i.close()
