from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import pandas as pd


class Inventory():

    @staticmethod
    def import_data(path, report_type):
        splited_path = path.split('.')
        exten = splited_path[len(splited_path) - 1]
        print(exten)
        if exten == "csv":
            df = pd.read_csv(path)

        if exten == "xml":
            df = pd.read_xml(path)
            print(df)

        if exten == "json":
            df = pd.read_json(path)

        if report_type == "simples":
            report = SimpleReport.generate(df)
            return report

        report = CompleteReport.generate(df)
        return report
