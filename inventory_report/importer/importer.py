from abc import ABC, abstractmethod
import csv


class Inporter(ABC):
    @abstractmethod
    def import_data(path):
        raise NotImplementedError


class CsvImporter(Inporter):
    def import_data(path):
        with open(path, mode="r") as file_reports:
            data_csv = csv.DictReader(file_reports)
            reports = list(
                report for report in data_csv
            )
            return reports

# print(CsvImporter.import_data("inventory_report/data/inventory.xml"))