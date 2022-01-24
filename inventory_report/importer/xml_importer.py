import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    """
    Implementação baseada em DATACAMP
    https://www.datacamp.com/community/tutorials/python-xml-elementtree?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034361&utm_targetid=aud-748597547652:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9102343&gclid=CjwKCAjw8KmLBhB8EiwAQbqNoEQpOBQUo9pIEujwiv7sdqFxImqFp8HpUXKrVFsOjxH618fgbhTLXBoCQHEQAvD_BwE
    """
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, mode="r") as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = [{col.tag: col.text for col in row} for row in root]
                return data
        raise ValueError("Arquivo inválido")
