
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        file_data = []

        with open(file_path) as file:
            # https://omz-software.com/pythonista/docs/ios/xmltodict.html
            for enterprise in xmltodict.parse(file.read())["dataset"][
                "record"
            ]:
                file_data.append(enterprise)

        return file_data
