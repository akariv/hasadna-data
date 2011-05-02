import os
FIELD_TYPE__SLUG        = 'slug'
FIELD_TYPE__INTEGER     = 'int'
FIELD_TYPE__FLOAT       = 'float'
FIELD_TYPE__STRING      = 'str'
FIELD_TYPE__REFERENCE   = 'ref'
FIELD_TYPE__BOOLEAN     = 'bool'
FIELD_TYPE__URL         = 'url'

class BaseField(object):
    FIELD_TYPE = 'none'

    def __init__(self,params):
        # params is a list of strings
        self.params = params
    
    def load(self,input):
        # input is the read value
        assert(False)
        
class NoneField(BaseField):
    
    def load(self,input):
        return None

class SlugField(BaseField):
    FIELD_TYPE = FIELD_TYPE__SLUG
    
    def load(self,input):
        return str(input)        

class IntegerField(BaseField):
    FIELD_TYPE = FIELD_TYPE__INTEGER

    def load(self,input):
        try:
            return int(input)
        except:     
            return None   

class FloatField(BaseField):
    FIELD_TYPE = FIELD_TYPE__FLOAT

    def load(self,input):
        try:
            return float(input)
        except:     
            return None   

class StringField(BaseField):
    FIELD_TYPE = FIELD_TYPE__STRING
    
    def load(self,input):
        return str(input) 

class RefField(BaseField):
    FIELD_TYPE = FIELD_TYPE__REFERENCE
    
    def load(self,input):
        if len(self.params) == 1:
            #TODO: This won't work on windows (fwd slashes only)
            return { '_ref' : os.path.join(self.params[0], str(input)) }
        return None

class BooleanField(BaseField):
    FIELD_TYPE = FIELD_TYPE__BOOLEAN
    
    TRUE_VALUES  = [ 'Y', 'y', 'T', 't', 'True', 'true', 'TRUE', 1, '1', ]
    FALSE_VALUES = [ 'N', 'n', 'F', 'f', 'False', 'false', 'FALSE', 0, '0', ]
    
    def load(self,input):
        if input in self.TRUE_VALUES:
            return True
        elif input in self.FALSE_VALUES:
            return False
        else:
            return None
            
class FieldLoader(object):

    FIELD_LOADERS = [ SlugField, 
                      IntegerField,
                      FloatField,
                      StringField,
                      RefField,
                      BooleanField,
                      ]
        
    def __init__(self,fields):
        self.loaders = {}
        self.none = NoneField([])
        for klass in self.FIELD_LOADERS:
            self.loaders[klass.FIELD_TYPE] = klass        
        self.fields = {}
        for k, v in fields.iteritems():
            if not ':' in v:
                v = v+':'
            field_type, params = v.split(':',1)
            params = params.split(',')
            self.fields[k] = self.loaders.get(field_type,NoneField)(params)
            if field_type == FIELD_TYPE__SLUG:
                self.slug_field = k
            
    def load_field(self,field,input):
        return self.fields.get(field,self.none).load(input)

    def extract_slug(self,rec):
        slug = rec[self.slug_field]
        del rec[self.slug_field]
        return slug
