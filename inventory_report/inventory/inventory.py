from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory(CompleteReport, SimpleReport):
    @classmethod
    def import_data(cls, path, report_type):
        extension_type = path.split(".")[1]

        if (extension_type == "csv"):
            return cls.import_data_csv(path, report_type)
        elif (extension_type == "json"):
            return cls.import_data_json(path, report_type)
        elif (extension_type == "xml"):
            return cls.import_data_xml(path, report_type)

    def import_data_csv(path, report_type):
        with open(path, mode="r") as file_reports:
            dict_from_csv = csv.DictReader(file_reports)
            reports = list(
                report for report in dict_from_csv
            )
            if report_type == "simples":
                return SimpleReport.generate(reports)
            elif report_type == "completo":
                return CompleteReport.generate(reports)

    def import_data_json(path, report_type):
        with open(path, mode="r") as file_reports:
            dict_from_json = json.load(file_reports)
            reports = list(
                report for report in dict_from_json
            )
            if report_type == "simples":
                return SimpleReport.generate(reports)
            elif report_type == "completo":
                return CompleteReport.generate(reports)

    def import_data_xml(path, report_type):
        with open(path) as file_reports:
            string_from_xml = xmltodict.parse(file_reports.read())
            file_reports.close()
            dict_from_string = json.dumps(string_from_xml)
            reports = json.loads(dict_from_string)["dataset"]["record"]
            if report_type == "simples":
                return SimpleReport.generate(reports)
            elif report_type == "completo":
                return CompleteReport.generate(reports)


# print(Inventory.import_data
# ("inventory_report/data/inventory.csv", "completo"))
