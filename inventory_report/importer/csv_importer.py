from .importer import Importer
import csv


class CSV_Importer(Importer):
    @classmethod
    def import_data(cls, path):
        data = []
        with open(path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                data.append(rows)
        return data
