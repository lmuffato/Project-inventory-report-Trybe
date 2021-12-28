import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith('.csv'):
            with open(path) as csv_file:
                data = list(csv.DictReader(csv_file))
        if path.endswith('.json'):
            with open(path) as json_file:
                data = json.load(json_file)
        # Esta parte foi consultada do meu proprio projeto
        # antigo da Turma 06 junto com o Thales
        if path.endswith('.xml'):
            with open(path) as xml_file:
                xml_dic = xmltodict.parse(xml_file.read())
                xml_json = json.dumps(xml_dic)
                data = json.loads(xml_json)['dataset']['record']
        # Fim da parte consultada!

        if type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
