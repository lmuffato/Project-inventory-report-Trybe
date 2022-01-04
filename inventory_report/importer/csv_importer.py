import csv


class Csv_importer:
    def import_csv(path):
        result = []
        with open(path) as csv_file:
            products_list = csv.DictReader(csv_file, delimiter=',')
            for product in products_list:
                result.append(product)
        return result
