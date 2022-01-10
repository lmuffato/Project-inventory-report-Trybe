# para o melhor entendimento dos requisitos e vizualizacao dos codigos,
# fiz uma pesquisa dentre varios projetos de colegas da turma
import csv
import xml.etree.ElementTree as ET
import json


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    __report_functions = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(file_path, report_type):
        array_data = []

        if file_path.endswith(".csv"):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                array_data = [row for row in reader]

        elif file_path.endswith(".json"):
            with open(file_path, "r") as file:
                array_data = json.load(file)

        elif file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root = tree.getroot()
            array_data = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]

        else:
            raise ValueError("Arquivo inválido")
        return Inventory.__report_functions[report_type](array_data)
