import json


class JsonImporter:
    @staticmethod
    def import_data(data):
        if data.endswith('.json'):
            with open(data) as file:
                return json.load(file)
        else:
            return (
                f'Invalido: {data}'
            )
