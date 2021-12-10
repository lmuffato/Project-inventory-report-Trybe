from datetime import datetime


class return_data:
    def newer_data(list):
        today = datetime.today().strftime('%Y-%m-%d')
        newer = list[0]['data_de_validade']
        for item in list:
            item_data = item['data_de_validade']
            if newer > item_data > today:
                newer = item_data
        return newer

    def older_data(list):
        older = list[0]['data_de_fabricacao']
        for item in list:
            item_data = item['data_de_fabricacao']
            if item_data < older:
                older = item_data
        return older
