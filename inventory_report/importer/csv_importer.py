from .importer import Importer
import csv
import os


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):

        file_name, extension = os.path.splitext(path)

        if extension != ".csv":
            raise ValueError("Arquivo inválido")

        data = []
        with open(path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                data.append(rows)
        return data
