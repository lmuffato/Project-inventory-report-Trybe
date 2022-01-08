from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        file_extension = path.split(".")[1]
        if file_extension == "xml":
            tree = ET.parse(path)
            root = tree.getroot()
            data = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
            return data
        else:
            raise ValueError("Arquivo inválido")
