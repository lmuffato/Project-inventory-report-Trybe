from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path, 'r') as file:
                data = csv.DictReader(file)
                return [*data]
        raise ValueError("Arquivo inválido")
