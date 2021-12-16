import csv

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        indexOfDot = path.find(".")
        firstLetterOfExtention = path(indexOfDot + 1)
        if firstLetterOfExtention("c"):
            with open(path) as file:
                data = csv.DictReader(file)
                return [*data]
        raise ValueError
