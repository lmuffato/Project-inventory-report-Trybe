import xml.etree.ElementTree as ET


class XmlImporter():
    def import_data(path):

        if path.endswith('.xml'):
            tree = ET.parse(path)
            dataset = tree.getroot()
            data = [{ elem.tag: elem.text  for elem in record } for record in dataset]
            return data
        raise ValueError('Arquivo inválido')