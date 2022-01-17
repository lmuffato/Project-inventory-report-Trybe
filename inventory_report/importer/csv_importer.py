from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(arq):
        arr = []
        if "csv" not in arq:
            raise(ValueError('Arquivo inválido'))
        with open(arq) as file:
            reader_file = csv.DictReader(file)
            for element in reader_file:
                arr.append(element)

        return arr
