import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        list = []
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for value in reader:
                list.append(value)
        return list

    @classmethod
    def import_data(cls, path, report_type):
        readers = {
            "csv": cls.read_csv
        }

        reports = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }

        file_format = path.split('.')[-1]
        list = readers[file_format](path)
        return reports[report_type](list)
