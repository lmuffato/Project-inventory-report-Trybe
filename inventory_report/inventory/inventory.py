import xml.etree.ElementTree as ET
import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


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
            from_xml = ET.parse(file_reports).getroot()
            list_from_xml = []
            index = 0
            for xml in from_xml:
                list_from_xml.append({})
                for element in xml:
                    list_from_xml[index][element.tag] = element.text
                index += 1
            if report_type == "simples":
                return SimpleReport.generate(list_from_xml)
            elif report_type == "completo":
                return CompleteReport.generate(list_from_xml)


# print(Inventory.import_data_xml
# ("inventory_report/data/inventory.xml", "completo"))
