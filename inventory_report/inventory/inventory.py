import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def send_report(report_type, data):
        if report_type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    def import_data(cls, path, report_type):
        if path.endswith('.csv'):
            with open(path) as file:
                csv_file = csv.DictReader(file)
                data = [line for line in csv_file]
                return cls.send_report(report_type, data)

        elif path.endswith('.json'):
            with open(path, 'r') as file:
                data = json.load(file)
                return cls.send_report(report_type, data)

        else:
            tree = ET.parse(path)
            dataset = tree.getroot()
            data = [
                {
                    el.tag: el.text
                    for el in record
                }
                for record in dataset
            ]
            return cls.send_report(report_type, data)
