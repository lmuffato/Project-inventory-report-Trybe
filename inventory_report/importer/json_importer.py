import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(arq):
        if "json" not in arq:
            raise(ValueError('Arquivo inválido'))

        with open(arq) as file:
            reader = file.read()
            reader_file = json.loads(reader)

        arr = [element for element in reader_file]

        return arr
