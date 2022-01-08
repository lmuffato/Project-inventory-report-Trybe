from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(self, path):
        with(open(path)) as file:
            return list(csv.DictReader(file))
