from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path) as file:
                dictionary_obj = csv.DictReader(file)
                dictionary_list = []
                for lists in dictionary_obj:
                    dictionary_list.append(lists)
            return dictionary_list
        else:
            raise ValueError('Arquivo inválido')
