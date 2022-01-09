import xmltodict
import json

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        extension_type = path.split(".")[1]
        # try:
        if (extension_type == "xml"):
            with open(path) as file_reports:
                string_from_xml = xmltodict.parse(file_reports.read())
                file_reports.close()
                dict_from_string = json.dumps(string_from_xml)
                reports = json.loads(dict_from_string)["dataset"]["record"]
                return reports
        # except ValueError:
        else:
            raise ValueError("Arquivo inválido")


# print(XmlImporter.import_data("inventory_report/data/inventory.csv"))
