from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        file_error = path.split('.')[-1]
        if file_error != 'csv':
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader = csv.DictReader(file)
            list = []
            for item in reader:
                list.append(item)
        print(list)
        return list
