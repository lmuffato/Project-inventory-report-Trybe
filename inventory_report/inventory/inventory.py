import csv
import json
import xmltodict
# https://linuxhint.com/python_xml_to_dictionary/


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(file_path):
        file_data = []
        with open(file_path) as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for enterprise in file_reader:
                file_data.append(enterprise)
        return file_data

    def import_json(file_path):
        file_data = []
        with open(file_path) as file:
            file_data = json.load(file)
        return file_data

    def import_xml(file_path):
        file_data = []
        with open(file_path) as file:
            # https://omz-software.com/pythonista/docs/ios/xmltodict.html
            for enterprise in xmltodict.parse(file.read())["dataset"][
                "record"
            ]:
                file_data.append(enterprise)
        return file_data

    @classmethod
    def import_data(cls, file_path, report_type="simples"):
        enterprises_list = []
        if file_path.endswith(".csv"):
            enterprises_list = cls.import_csv(file_path)
        elif file_path.endswith(".json"):
            enterprises_list = cls.import_json(file_path)
        elif file_path.endswith(".xml"):
            enterprises_list = cls.import_xml(file_path)
        if report_type == "simples":
            return SimpleReport.generate(enterprises_list)
        return CompleteReport.generate(enterprises_list)


Inventory.import_xml("inventory_report/data/inventory.xml")
