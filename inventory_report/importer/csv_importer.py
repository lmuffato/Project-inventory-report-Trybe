from inventory_report.importer.importer import Importer
import csv
from pathlib import Path


class CsvImporter(Importer):
    def check_extension(path):
        ext = Path(path).suffix
        if(ext != '.csv'):
            raise ValueError('Arquivo inválido')

    def import_data(path):
        CsvImporter.check_extension(path)

        with(open(path)) as file:
            return list(csv.DictReader(file))
