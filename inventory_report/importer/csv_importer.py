import csv


class CsvImporter:
    def import_csv_file(path):
        content = []

        with open(path) as file:
            lists = csv.DictReader(file, delimiter=",")
            for list in lists:
                content.append(list)
        return content
