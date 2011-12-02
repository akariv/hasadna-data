import os
FIELD_TYPE__SLUG        = 'slug'
FIELD_TYPE__INTEGER     = 'int'
FIELD_TYPE__FLOAT       = 'float'
FIELD_TYPE__STRING      = 'str'
FIELD_TYPE__SEPSTRING   = 'sepstr'
FIELD_TYPE__REFERENCE   = 'ref'
FIELD_TYPE__REF_LIST    = 'reflist'
FIELD_TYPE__BOOLEAN     = 'bool'
FIELD_TYPE__URL         = 'url'
FIELD_TYPE__OBJECT      = 'object'
FIELD_TYPE__FILE        = 'file'

class BaseField(object):
    FIELD_TYPE = 'none'
   
    @classmethod
    def load(cls,input):
        # input is the read value
        assert(False)
        
class NoneField(BaseField):
    
    @classmethod
    def load(cls,input):
        return None

class SlugField(BaseField):
    FIELD_TYPE = FIELD_TYPE__SLUG
    
    @classmethod
    def load(cls,input):
        if type(input) == unicode:
            return input 
        else:
            return unicode(input.decode('utf8')) 

class IntegerField(BaseField):
    FIELD_TYPE = FIELD_TYPE__INTEGER

    @classmethod
    def load(cls,input):
        try:
            return int(input)
        except:     
            return None   

class FloatField(BaseField):
    FIELD_TYPE = FIELD_TYPE__FLOAT

    @classmethod
    def load(cls,input):
        try:
            return float(input)
        except:     
            return None   

class StringField(BaseField):
    FIELD_TYPE = FIELD_TYPE__STRING
    
    @classmethod
    def load(cls,input):
        if type(input) == unicode:
            return input 
        else:
            return unicode(input.decode('utf8')) 

class SeparatedStringField(BaseField):
    FIELD_TYPE = FIELD_TYPE__SEPSTRING
    
    @classmethod
    def load(cls,input):
        if type(input) != unicode:
            input = unicode(input.decode('utf8')) 
        input = input.split(';')
        input = [ x.strip() for x in input ]
        return input

class RefField(BaseField):
    FIELD_TYPE = FIELD_TYPE__REFERENCE
    
    @classmethod
    def load(cls,input,ref):
        if input == None or len(input) == 0:
            return None
        else:
            return { '_ref' : os.path.join(ref, str(input)) }

class RefListField(BaseField):
    FIELD_TYPE = FIELD_TYPE__REF_LIST
    
    @classmethod
    def load(cls,input,ref):
        if input == None or len(input) == 0:
            return []
        else:
            if type(input) in [ str, unicode ]:
                input = input.split(',') 
            if type(input) == list:
                return [ { '_ref' : os.path.join(ref, str(i)) } for i in input ]
            else:
                return []

class BooleanField(BaseField):
    FIELD_TYPE = FIELD_TYPE__BOOLEAN
    
    TRUE_VALUES  = [ 'Y', 'y', 'T', 't', 'True', 'true', 'TRUE', 1, '1', True]
    FALSE_VALUES = [ 'N', 'n', 'F', 'f', 'False', 'false', 'FALSE', 0, '0', False ]
    
    @classmethod
    def load(cls,input):
        if input in cls.TRUE_VALUES:
            return True
        elif input in cls.FALSE_VALUES:
            return False
        else:
            return None

class ObjectField(BaseField):
    FIELD_TYPE = FIELD_TYPE__OBJECT
        
    @classmethod
    def load(cls,input):
        return input

class FileField(BaseField):
    FIELD_TYPE = FIELD_TYPE__FILE
        
    @classmethod
    def load(cls,input):
        return file(input).read()
            
class FieldLoader(object):

    FIELD_LOADERS = [ SlugField, 
                      IntegerField,
                      FloatField,
                      StringField,
                      RefField,
                      RefListField,
                      BooleanField,
                      ObjectField,
                      FileField
                      ]
        
    def __init__(self):
        self.loaders = {}
        for klass in self.FIELD_LOADERS:
            self.loaders[klass.FIELD_TYPE] = klass        
            
    def load_field(self,field,input):
        field_type = field['type']
        field_params = field.get('params',[])
        if self.loaders.has_key(field_type):
            return self.loaders[field_type].load(input,*field_params)
        else:
            return None
        
field_loader = FieldLoader()
