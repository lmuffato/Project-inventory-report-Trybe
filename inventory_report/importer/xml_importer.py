# Source:
# https://stackoverflow.com/questions/38869381/python-convert-xml-to-list
import xml.etree.ElementTree as etree

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        indexOfDot = path.find(".") + 1
        firstLetterOfExtention = path[indexOfDot]
        if firstLetterOfExtention == "x":
            lista = []
            tree = etree.parse(path)
            root = tree.getroot()
            for child in root.findall('record'):
                child_data = {}
                for data in child:
                    child_data[data.tag] = data.text
                lista.append(child_data)
            return lista
        else:
            raise ValueError('Arquivo inválido')
