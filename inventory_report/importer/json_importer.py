from inventory_report.importer.importer import Importer
from json import decoder
from pathlib import Path


class JsonImporter(Importer):
    decoder = decoder.JSONDecoder()

    def check_extension(path):
        ext = Path(path).suffix
        if(ext != '.json'):
            raise ValueError('Arquivo inválido')
    
    def import_data(path):
        JsonImporter.check_extension(path)

        out = ''
        with(open(path)) as x:
            out = x.read()
        return JsonImporter.decoder.decode(out)
    
