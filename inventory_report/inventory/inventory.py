from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory(CompleteReport, SimpleReport):
    def import_data(path, report_type):
        with open(path, mode="r") as file_reports:
            dict_from_csv = csv.DictReader(file_reports)
            reports = list(
                report for report in dict_from_csv
            )
            if report_type == "simples":
                return SimpleReport.generate(reports)
            elif report_type == "completo":
                return CompleteReport.generate(reports)
