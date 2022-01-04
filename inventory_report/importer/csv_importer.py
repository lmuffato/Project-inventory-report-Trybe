import csv

from inventory_report.importer.importer import Importer

# list = '../data/inventory.csv'


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            try:
                with open(path, "r") as file:
                    data = csv.DictReader(file)
                    return [*data]
                    """
                    Quando um * está presente no desempacotamento,
                    os valores são desempacotados em formato de lista.
                    """
            except OSError:
                print("arquivo inexistente")
        raise ValueError("Arquivo inválido")


# print(CsvImporter.import_data(list))
