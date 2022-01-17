import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(arq, type):
        arr = []
        with open(arq) as file:
            if "csv" in arq:
                reader_file = csv.DictReader(file)
            elif "json" in arq:
                reader = file.read()
                reader_file = json.loads(reader)
            else:
                string_xml = "".join(file)
                reader_xml = xmltodict.parse(string_xml)
                xml_convert_json = json.dumps(reader_xml)
                reader_file = json.loads(xml_convert_json)["dataset"]["record"]

            for element in reader_file:
                arr.append(element)

        if type == "simples":
            return SimpleReport.generate(arr)
        else:
            return CompleteReport.generate(arr)
