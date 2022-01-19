from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):  # implementando o método abstrato
        if (path.endswith('xml')):
            tree = ET.parse(path)
            root = tree.getroot()  # Raiz, tag principal
            stock = [
                {elemento.tag: elemento.text for elemento in record}
                # Lista os elementos filhos de record: nome e texto
                for record in root.findall('record')  # buscar tags record
                # record, são as tags que contem os elementos com texto
            ]
            return stock
        else:
            raise(ValueError('Arquivo inválido'))

# Teste manual
# readXml = XmlImporter.import_data('inventory_report/data/inventory.xml')
# print(readXml)
