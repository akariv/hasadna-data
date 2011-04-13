import os
from loaders import Loader
from db_loader import DBLoader

DATA_ROOT = os.path.realpath('../data/')

if __name__=="__main__":
    
    print "Loading data from %s" % DATA_ROOT
    
    for dirpath, dirnames, filenames in os.walk(DATA_ROOT):
        for f in filenames:
            filename = os.path.join(dirpath,f)
            loader = Loader.get_loader_for_filename(filename)
            if loader != None:
                relpath = os.path.realpath(dirpath).replace(os.path.realpath(DATA_ROOT),'')
                print "Processing %s, %s" % (relpath, f)
                
                db_loader = DBLoader(relpath,loader.get_field_types())
                db_loader.del_collection()
                for rec in loader.get_rows():
                    db_loader.new_item(rec)