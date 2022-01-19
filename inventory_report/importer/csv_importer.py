from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):  # implementando o método abstrato
        if (path.endswith('csv')):
            stock = []
            with open(path) as file:
                stock_csv = csv.DictReader(file)
                for elemento in stock_csv:
                    stock.append(elemento)
            return stock
        else:
            raise(ValueError('Arquivo inválido'))

# Teste manual
# ReadCsv = CsvImporter.import_data('inventory_report/data/inventory.csv')
# print(ReadCsv)
