from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file):
        path = file.split('.')
        extension = path[-1]
        if (extension != "csv"):
            raise ValueError("Arquivo inválido")
        with open(file) as csvfile:
            file_read = csv.DictReader(csvfile)
            return [row for row in file_read]
          
