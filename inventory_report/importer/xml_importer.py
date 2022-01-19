import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def get_xml_data(cls, root, content):
        for rec in root.findall("record"):
            id = rec.find("id").text
            nome_do_produto = rec.find("nome_do_produto").text
            nome_da_empresa = rec.find("nome_da_empresa").text
            data_de_fabricacao = rec.find("data_de_fabricacao").text
            data_de_validade = rec.find("data_de_validade").text
            numero_de_serie = rec.find("numero_de_serie").text
            instrucoes_de_armazenamento = rec.find(
                "instrucoes_de_armazenamento").text
            content.append({
                "id": id,
                "nome_do_produto": nome_do_produto,
                "nome_da_empresa": nome_da_empresa,
                "data_de_fabricacao": data_de_fabricacao,
                "data_de_validade": data_de_validade,
                "numero_de_serie": numero_de_serie,
                "instrucoes_de_armazenamento": instrucoes_de_armazenamento
            })

    @classmethod
    def import_data(self, path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        content = []
        tree = ET.parse(path)
        root = tree.getroot()
        self.get_xml_data(root, content)
        # print(content)
        return content
