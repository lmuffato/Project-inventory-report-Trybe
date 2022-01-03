import csv


class CsvImporter():
    def import_data(path):
        data = []

        if path.endswith('.csv'):
            with open(path, mode='r') as file:
                lists = csv.DictReader(file)

                for d in lists:
                    data.append(d)

            return data
        raise ValueError('Arquivo inválido')