import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        products = []
        fileType = path.split('.')[-1]

        if (fileType != 'xml'):
            raise(ValueError('Arquivo inválido'))

        with open(path) as file:
            products_xml = ET.parse(file).getroot()
            for product in products_xml:
                products.append({
                                    product[0].tag: product[0].text,
                                    product[1].tag: product[1].text,
                                    product[2].tag: product[2].text,
                                    product[3].tag: product[3].text,
                                    product[4].tag: product[4].text,
                                    product[5].tag: product[5].text,
                                    product[6].tag: product[6].text,
                                })
        return products
