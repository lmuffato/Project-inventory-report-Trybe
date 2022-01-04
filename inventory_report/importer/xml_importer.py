from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
            pass
