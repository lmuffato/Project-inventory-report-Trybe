from inventory_report.importer.importer import Importer
import pandas as pd


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        splited_path = path.split('.')
        exten = splited_path[len(splited_path) - 1]
        if exten != 'xml':
            raise ValueError('Arquivo inválido')
        df = pd.read_xml(path)
        s = list(df.T.to_dict().items())
        to_return = []
        for dir in s:
            dir[1]['id'] = str(dir[1]['id'])
            to_return.append(dir[1])
        return to_return
