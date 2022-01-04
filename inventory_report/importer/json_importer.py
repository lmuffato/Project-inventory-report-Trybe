import json

from inventory_report.importer.importer import Importer

# list = '../data/inventory.json'


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            try:
                with open(path, "r") as file:
                    data = json.load(file)
                    return data
            except OSError:
                print("arquivo inexistente")
        raise ValueError("Arquivo inválido")


# print(JsonImporter.import_data(list))
