from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json


class Inventory:
    def read_JSON(path):
        with open(path) as file:
            list = json.load(file)
        return list

    def check_type(self, path):
        if ".json" in path:
            return self.read_JSON(path)
        else:
            breakpoint

    @classmethod
    def import_data(self, path, type):
        list = self.check_type(self, path)

        if type == "completo":
            return CompleteReport.generate(list)
        else:
            return SimpleReport.generate(list)
