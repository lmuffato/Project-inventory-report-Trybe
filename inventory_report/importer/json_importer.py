from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith("json"):
            with open(path) as file:
                content = file.read()
                dictionary_list = json.loads(content)
            return dictionary_list
        else:
            raise ValueError("Arquivo inválido")
