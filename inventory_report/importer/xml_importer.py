import xml.etree.ElementTree as ET


class XmlImporter:
    def import_xml_file(path):
        if path.endswith("xml"):
            tree = ET.parse(path)
            root = tree.getroot()
            result = [
              {
                elem.tag: elem.text for elem in record
              }
              for record in root
            ]
            return result
