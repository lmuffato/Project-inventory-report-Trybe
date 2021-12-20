import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        indexOfDot = path.find(".") + 1
        firstLetterOfExtention = path[indexOfDot]
        if firstLetterOfExtention == "j":
            with open(path, mode="r") as file:
                data = json.load(file)
                return data
        raise ValueError('Arquivo inválido')
