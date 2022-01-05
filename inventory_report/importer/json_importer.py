import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith('.json'):
            raise ValueError('Invalid file extension')
        else:
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                return data
