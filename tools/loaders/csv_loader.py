from base import Loader
import csv

@Loader.loader
class CsvLoader(Loader):
    
    @classmethod
    def condition(cls,filename):
        return filename.endswith('.csv')
    
    def initialize(self,input_file):
        self.csv = csv.reader(input_file)
        self.field_names = self.csv.next()
    
    def get_rows(self):
        for r in self.csv:
            yield dict(zip(self.field_names,r))
