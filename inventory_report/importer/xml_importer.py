import json
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(arq):
        if "xml" not in arq:
            raise(ValueError('Arquivo inválido'))

        with open(arq) as file:
            string_xml = "".join(file)
            reader_xml = xmltodict.parse(string_xml)
            xml_convert_json = json.dumps(reader_xml)
            reader_file = json.loads(xml_convert_json)["dataset"]["record"]

        arr = [element for element in reader_file]

        return arr
