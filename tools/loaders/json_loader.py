from base import Loader
import json

@Loader.loader
class JsonLoader(Loader):
    
    @classmethod
    def condition(cls,filename):
        return filename.endswith('.json')
    
    def initialize(self,input_file):
        self.data = json.load(input_file)
    
    def get_rows(self):
        return self.data
