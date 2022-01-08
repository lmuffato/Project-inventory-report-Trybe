import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        file_extension = path.split(".")[1]
        if file_extension == "json":
            with open(path) as file:
                data = json.load(file)
                return data
        else:
            raise ValueError("Arquivo inválido")
