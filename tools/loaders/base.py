
class Loader(object):
    
    available_loaders = []
        
    @classmethod
    def condition(cls,filename):
        return False
    
    def initialize(self,input_file):
        assert(False)
    
    def get_field_types(self):
        assert(False)

    def get_rows(self):
        assert(False)

    @classmethod
    def loader(cls,klass):
        cls.available_loaders.append(klass)
        return klass
    
    @classmethod
    def get_loader_for_filename(cls,filename):
        for L in cls.available_loaders:
            if L.condition(filename):
                l = L()
                l.initialize(file(filename))
                return l
        return None
