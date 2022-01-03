from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        path = file.split('.')
        extension = path[-1]
        if (extension != "csv"):
            raise ValueError('Arquivo inválid')
