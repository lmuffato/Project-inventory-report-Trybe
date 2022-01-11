from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
from ..importer.csv_importer import CsvImporter
from ..importer.xml_importer import XmlImporter
from ..importer.json_importer import JsonImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            response = CsvImporter.import_data(path)
        elif "xml" in path:
            response = XmlImporter.import_data(path)
        elif "json" in path:
            response = JsonImporter.import_data(path)
        return cls.report_type(type, response)

    def report_type(type, report):
        if type == 'simples':
            return SimpleReport.generate(report)
        if type == 'completo':
            return CompleteReport.generate(report)
    pass

# Source:
# Sobre classmethod
# https://python-reference.readthedocs.io/en/latest/docs/functions/classmethod.html
# https://www.tutorialsteacher.com/python/classmethod-decorator
# Documentação Python
# https://docs.python.org/3/library/functions.html#classmethod
# Sobre herança:
# https://algoritmosempython.com.br/cursos/programacao-python/heranca/
