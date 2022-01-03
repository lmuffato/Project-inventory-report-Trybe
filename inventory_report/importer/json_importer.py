import re
import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(filepath):
        isJson = re.search(".json$", filepath)

        if not isJson:
            raise ValueError("Arquivo inválido")

        with open(filepath) as file:
            data = json.load(file)
            return data
