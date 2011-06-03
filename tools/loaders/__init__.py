import glob

from base import Loader

for f in glob.glob('loaders/*py'):
    __import__(f.replace("/",".").replace(".py",""))
