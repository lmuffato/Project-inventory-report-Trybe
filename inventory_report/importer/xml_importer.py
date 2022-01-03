import re
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(filepath):
        isXml = re.search(".xml$", filepath)

        if not isXml:
            raise ValueError("Arquivo inválido")

        file_data = []
        with open(filepath) as file:
            # https://omz-software.com/pythonista/docs/ios/xmltodict.html
            for enterprise in xmltodict.parse(file.read())["dataset"][
                "record"
            ]:
                file_data.append(enterprise)
        return file_data
