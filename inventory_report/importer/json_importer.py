from inventory_report.importer.importer import Importer
import json


# forma de passar o erro vista no repositório do André Sartoreto
# https://github.com/tryber/sd-010-a-inventory-report/pull/39
class JsonImporter(Importer):

    @classmethod
    def import_data(self, path):
        if path.endswith("json"):
            file = open(path, "r")
            data = json.load(file)
            return data
        else:
            raise ValueError("Arquivo inválido")
