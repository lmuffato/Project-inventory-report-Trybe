import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def send_report(report_type, data):
    if report_type == 'simples':
        return SimpleReport.generate(data)
    else:
        return CompleteReport.generate(data)


class Inventory:
    def import_data(path, report_type):
        if path.endswith('.csv'):
            with open(path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [line for line in csv_reader]
                return send_report(report_type, data)

        elif path.endswith('.json'):
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                return send_report(report_type, data)
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
            if report_type == 'simples':
                return SimpleReport.generate(data)
            else:
                return CompleteReport.generate(data)
