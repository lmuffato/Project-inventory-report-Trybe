from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    def __init__(cls, simple_report=SimpleReport()):
        cls.simple_report = simple_report

    def generate(cls, list):
        simple_report = cls.simple_report.generate(list)
