import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(fileName):
        returndict = []
        if not fileName.endswith('csv'):
            raise ValueError("Arquivo inválido")
        with open(fileName, newline='') as csvFile:
            readed = csv.DictReader(csvFile)
            for row in readed:
                returndict.append(row)
        return returndict
