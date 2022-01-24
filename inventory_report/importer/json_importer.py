import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    """
    Implementação baseada em DATACAMP
    https://www.datacamp.com/community/tutorials/json-data-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034361&utm_targetid=aud-748597547652:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9102343&gclid=CjwKCAjw8KmLBhB8EiwAQbqNoGDmbV1FS3YyqlyYzxI8yuuIuDMno-NaMQx21DrXuwyOMQ9ERsLR_xoCtBcQAvD_BwE
    """
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                data = json.load(file)
                return data
        raise ValueError("Arquivo inválido")
