from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json
import csv
import xmltodict


class FormatTypes():
    @classmethod
    def type_json(cls, path):
        with open(path, mode='r') as file:
            return json.load(file)

    @classmethod
    def type_csv(cls, path):
        data = []
        with open(path) as file:
            list_csv = csv.DictReader(file, delimiter=',')
            for line in list_csv:
                data.append(line)
        return data

    @classmethod
    def type_xml(cls, path):
        with open(path) as file:
            result = xmltodict.parse(file.read())
        data = [dict(line) for line in result['dataset']['record']]
        return data


class TypesReturn():
    @classmethod
    def type_return(cls, list_prod, type):
        if type == 'simples':
            simples = SimpleReport.generate(list_prod)
            return simples
        elif type == 'completo':
            completo = CompleteReport.generate(list_prod)
            return completo


class Inventory():
    @classmethod
    def import_data(cls, path, type):
        if path.endswith('.json'):
            list_prod = FormatTypes.type_json(path)
        elif path.endswith('.csv'):
            list_prod = FormatTypes.type_csv(path)
        elif path.endswith('xml'):
            list_prod = FormatTypes().type_xml(path)
        else:
            return 'Incorrect Path'

        result = TypesReturn.type_return(list_prod, type)
<<<<<<< HEAD
        return result
=======
        return 
>>>>>>> paulovitorInventoryReport
