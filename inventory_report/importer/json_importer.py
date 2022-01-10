# para o melhor entendimento dos requisitos e vizualizacao dos codigos.
# fiz uma pesquisa dentre varios projetos de colegas da turma.
# Feito por minha dupla Nathalia Zebral
from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        if file_path.endswith(".json"):
            with open(file_path, "r") as jsonfile:
                return json.load(jsonfile)

        raise ValueError("Arquivo inválido")
