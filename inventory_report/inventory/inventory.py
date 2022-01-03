from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory():

    def read_file(path):
        with open(path) as file:
            if('csv' in path):
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
            if('json' in path):
                data = json.load(file)
            if('xml' in path):
                doc = xmltodict.parse(file.read())
                data = []
                for r in doc['dataset']['record']:
                    data.append(r)
            return data

    def import_data(path, report_type):
        data = Inventory.read_file(path)
        if(report_type == 'simples'):
            simple = SimpleReport.generate(data)
            return simple
        if(report_type == 'completo'):
            complete = CompleteReport.generate(data)
            return complete
