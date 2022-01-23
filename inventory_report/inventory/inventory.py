import csv
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from collections import Counter


def find_date_factory(list):
    format_date = datetime.now().strftime('%Y-%m-%d')
    date = [
        product["data_de_validade"]
        for product in list
        if product["data_de_validade"] >= format_date
    ]
    date.sort()
    return date[0]


def find_data_valid(list):
    return min(product["data_de_fabricacao"] for product in list)


def find_company_max_amount(list):
    return max(company["nome_da_empresa"] for company in list)


class Inventory:
    def return_company_stock_qty(list):
        result = ''

        company_group = [company["nome_da_empresa"] for company in list]
        quant = Counter(company_group)

        for company_group_name in quant:
            result += f"- {company_group_name}: {quant[company_group_name]}\n"

        return f"Produtos estocados por empresa: \n{result}"

    def generate_complete(cls, list):
        generate_simple_report = cls.generate_simple(list)
        result = cls.return_company_stock_qty(list)
        return f"{generate_simple_report}\n{result}"

    def generate_simple(list):
        date_factory = find_data_valid(list)
        date_valid = find_date_factory(list)
        company_max_amount = find_company_max_amount(list)

        return (
            f"Data de fabricação mais antiga: {date_factory}\n"
            f"Data de validade mais próxima: {date_valid}\n"
            f"Empresa com maior quantidade"
            f" de produtos estocados: {company_max_amount}\n"
        )

    def send_report(cls, type):
        report_type = {
            'simples': cls.generate_simple,
            'completo': cls.generate_complete,
        }
        return report_type[type]

    def import_data(path, report_type):
        if path.endswith('.csv'):
            with open(path) as file:
                csv_file = csv.DictReader(file)
                data = [line for line in csv_file]
                return Inventory.send_report(report_type)(data)

        elif path.endswith('.json'):
            with open(path) as file:
                data = json.load(file)
                return Inventory.send_report(report_type)(data)

        else:
            tree = ET.parse(path)
            dataset = tree.getroot()
            data = [
                {
                    el.tag: el.text
                    for el in record
                }
                for record in dataset
            ]
            return Inventory.send_report(report_type)(data)
