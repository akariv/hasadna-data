from base import Loader
import json

@Loader.loader
class JsonsLoader(Loader):
    
    @classmethod
    def condition(cls,filename):
        return filename.endswith('.jsons')
    
    def initialize(self,input_file):
        self.file = input_file
    
    def get_rows(self):
        for line in self.file:
            yield json.loads(line)
