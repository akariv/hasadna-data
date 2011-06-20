import os
import sys
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
    
    try:
        file('/tmp/mylock').read()
        print "Found lock file"
        sys.exit(0)
    except Exception, e:
        f = file('/tmp/mylock','w')
        print "Created lock file"
        f.write('bla')
        f.close()
    
    saved_stat = shelve.open('saved_state')
    
    to_process = [ '/data' ]

    try:    
        while len(to_process) > 0:
                   
            relpath = to_process.pop(0)
            
            desc = os.path.join(DATA_ROOT, relpath[1:], DESCRIPTION_FILE )
    
            print "description file %s" % desc        
            description = json.loads(file(desc).read())

            path, slug = os.path.dirname(relpath), os.path.basename(relpath)
            #print ">>>>>>>",path,slug,description
            
            print "\tloading templates"
            templates = description.get("templates",{})
            for k,v in templates.iteritems(): # k=name, v=filename
                templates[k] = file(os.path.join(DATA_ROOT, relpath[1:], v)).read()
            description["templates"] = templates

            print "\tloading statics"
            statics = description.get("statics",{})
            for k,v in statics.iteritems():  # k=filename, v=content-type
                statics[k] = [ v, file(os.path.join(DATA_ROOT, relpath[1:], v)).read() ]
            description["statics"] = templates
    
            DBLoader.new_item(path,slug,description)
            
            if description.has_key('subcatalogs'):
                to_process.extend( [ os.path.join( relpath, x) for x in description['subcatalogs'] ] )
            elif description.has_key('datafile'):
                                
                path = os.path.join( DATA_ROOT, relpath[1:] )
                curdir = os.path.realpath(os.path.curdir)
                print "\tpath = %s, curdir = %s" % (path, curdir)
                try:
                    os.chdir(path)
                    print "in %s" % os.path.realpath(os.path.curdir)
                    filename = description['datafile']
                    full_filename = str(os.path.join(path,filename))
                    
                    file_stat, to_skip = saved_stat.get(full_filename,(0,0))
                    
                    fields = description['fields']   
                        
                    print "\tdata file %s" % filename
                
                    loader = Loader.get_loader_for_filename(filename,fields)
                    if loader != None:
                        
                        if calc_stat(filename) != file_stat:
                            to_skip = 0
                            #DBLoader.del_collection(relpath)
        
                        slugs = DBLoader.get_slugs(relpath)
                        
                        print "\tProcessing %s, %s" % (relpath, description['datafile'] )
                        print "\tDB already has %d slugs" % len(slugs)
                        print "\tskipping %s records" % to_skip        
        
                        filename_stat = calc_stat(filename)
                        
                        num_rows = 0
                        saved_stat[full_filename] = filename_stat, to_skip
                        for slug,rec in loader.get_processed_rows():
                            if num_rows >= to_skip:
                                print "\t\tLoading: slug = %s, row = %s" % (slug, rec)
                                DBLoader.new_item(relpath,slug,rec)
                            slugs.discard(slug)
                            num_rows += 1
                            saved_stat[full_filename] = calc_stat(filename), num_rows
                        
                        for slug in slugs:
                            print "\t\tremaining slug: %s/%s" % (relpath,slug)
                            
                except Exception,e:
                    print "got here somehow %r" % e
                    raise
                finally:
                    os.chdir(curdir)
                    
    except:
        raise
    finally:
        os.unlink('/tmp/mylock')
