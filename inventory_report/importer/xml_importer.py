# para o melhor entendimento dos requisitos e vizualizacao dos codigos
# fiz uma pesquisa dentre varios projetos de colegas da turma.
from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(file_path):
        if file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root = tree.getroot()
            return [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
        raise ValueError("Arquivo inválido")
