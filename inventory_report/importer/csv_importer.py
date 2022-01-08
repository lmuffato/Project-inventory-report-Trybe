# commit
import csv

from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_informations = cls.get_file_informations(path)

        if file_informations["file_type"] == ".csv":
            with open(path) as file:
                file_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )

                return [stock for stock in file_reader]
        else:
            raise ValueError("Arquivo inválido")
