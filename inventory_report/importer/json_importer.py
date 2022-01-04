import json


class JsonImporter:
    def import_data(path):
        data = []

        if path.endswith(".json"):
            with open(path, mode="r") as file:
                lists = json.load(file)

                for d in lists:
                    data.append(d)

            return data
        raise ValueError("Arquivo inválido")
