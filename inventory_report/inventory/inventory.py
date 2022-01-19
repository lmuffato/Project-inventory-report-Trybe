import csv


class Inventory:
    def import_data(file):
        if ".csv" in file:
            with open(file) as data:
                return list(csv.DictReader(data))
        raise ValueError("Arquivo inválido")
