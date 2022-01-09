import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        extension_type = path.split(".")[1]
        if (extension_type == "xml"):
            with open(path) as file_reports:
                from_xml = ET.parse(file_reports).getroot()
                list_from_xml = []
                index = 0
                for xml in from_xml:
                    list_from_xml.append({})
                    for element in xml:
                        list_from_xml[index][element.tag] = element.text
                    index += 1
                return list_from_xml
        else:
            raise ValueError("Arquivo inválido")


# print(XmlImporter.import_data("inventory_report/data/inventory.csv"))
