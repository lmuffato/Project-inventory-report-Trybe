from inventory_report.importer.importer import Importer
from json import decoder


class JsonImporter(Importer):
    decoder = decoder.JSONDecoder()
    
    def import_data(self, path):
        out = ''
        with(open(path)) as x:
            out = x.read()
        return self.decoder.decode(out)
    
