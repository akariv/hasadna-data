from field_loaders import field_loader, FIELD_TYPE__SLUG
import sys

class Loader(object):
    
    available_loaders = []

    def __init__(self,fields):
        self.fields = fields
        self.slug_field = None
        for k, v in self.fields.iteritems():
            print k,v
            if v['type'] == FIELD_TYPE__SLUG:
                self.slug_field = k
        
    @classmethod
    def condition(cls,filename):
        return False
    
    def initialize(self,input_file):
        assert(False)

    def get_rows(self):
        assert(False)
    
    def compress_parts(self,row):        
        rec = {}
        for k, v in row.iteritems():
            d = rec
            parts = k.split('.')
            for part in parts[:-1]:
                d = rec.setdefault(part,{})
            d[parts[-1]] = v
        return rec 

    def load_fields(self,row):
        rec = {}
        for k, v in row.iteritems():
            fieldname = k.split('.')[0]
            field = self.fields.get(fieldname)
            if field != None:
                rec[k] = field_loader.load_field(field,v)
        return rec 
    
    def extract_slug(self,row):
        if self.slug_field != None:
            slug = row.get(self.slug_field,None)
            if slug != None:
                del row[self.slug_field]
                return slug, row
        return None, None

    def get_processed_rows(self):
        for row in self.get_rows():
            row = self.load_fields(row)
            row = self.compress_parts(row)
            slug, row = self.extract_slug(row)
            print "-- 3: slug = %s, row = %s" % (slug, row)
            yield slug, row

    @classmethod
    def loader(cls,klass):
        cls.available_loaders.append(klass)
        return klass
    
    @classmethod
    def get_loader_for_filename(cls,filename,fields):
        for L in cls.available_loaders:
            if L.condition(filename):
                l = L(fields)
                l.initialize(file(filename))
                return l
        return None
