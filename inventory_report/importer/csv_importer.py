import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        file_extension = path.split(".")[1]
        if file_extension == "csv":
            with open(path) as file:
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
                return data
        else:
            raise ValueError("Arquivo inválido")
