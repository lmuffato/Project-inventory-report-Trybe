import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        extension_type = path.split(".")[1]
        if (extension_type == "json"):
            with open(path, mode="r") as file_reports:
                dict_from_json = json.load(file_reports)
                reports = list(
                    report for report in dict_from_json
                )
                return reports
        else:
            raise ValueError("Arquivo inválido")
