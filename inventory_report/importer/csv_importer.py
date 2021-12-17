import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        indexOfDot = path.find(".") + 1
        firstLetterOfExtention = path[indexOfDot]
        if firstLetterOfExtention == "c":
            with open(path) as file:
                data = csv.DictReader(file)
                return [*data]
        raise ValueError
