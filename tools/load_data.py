import os
from loaders import Loader
from db_loader import DBLoader
import json
import shelve

DATA_ROOT = os.path.realpath('..')
DESCRIPTION_FILE = 'description.json'

def calc_stat(filename):
    st = os.stat(filename)
    return "%s %s" % ( st.st_size, st.st_mtime )

if __name__=="__main__":
    
    print "Loading data from %s" % DATA_ROOT
    
    saved_stat = shelve.open('saved_state')
    
    to_process = [ '/data' ]
    
    while len(to_process) > 0:
               
        relpath = to_process.pop(0)
        
        desc = os.path.join(DATA_ROOT, relpath[1:], DESCRIPTION_FILE )

        print "description file %s" % desc        
        description = json.loads(file(desc).read())

        path, slug = os.path.dirname(relpath), os.path.basename(relpath)
        print ">>>>>>>",path,slug,description
        DBLoader.new_item(path,slug,description)
        
        if description.has_key('subcatalogs'):
            to_process.extend( [ os.path.join( relpath, x) for x in description['subcatalogs'] ] )
        elif description.has_key('datafile'):
            filename = os.path.join( DATA_ROOT, relpath[1:], description['datafile'] )
            filename = str(filename)
            
            if calc_stat(filename) != saved_stat.get(filename):
                            
                fields = description['fields']   
                
                loader = Loader.get_loader_for_filename(filename,fields)
                if loader != None:
                    print "Processing %s, %s" % (relpath, description['datafile'] )
                    DBLoader.del_collection(relpath)
                    
                    for slug,rec in loader.get_processed_rows():
                        DBLoader.new_item(relpath,slug,rec)
                        
                    saved_stat[filename] = calc_stat(filename) 
