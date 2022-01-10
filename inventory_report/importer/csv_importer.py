import csv


class CsvImporter:
    @staticmethod
    def import_data(data):
        if data.endswith('.csv'):
            with open(data) as file:
                return list(csv.DictReader(file))
        else:
            return (
                f'Invalido: {data}'
            )
