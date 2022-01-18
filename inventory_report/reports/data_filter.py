from datetime import datetime


class DateFilter:
    def oldest_date(stock):
        data_mais_antiga = [  # cria um array com a iteração de cada elemento
          data['data_de_fabricacao']  # cada elemento receber esse [valor]
          for data in stock  # O evento ocorre em cada elem do stock
        ]
        return min(data_mais_antiga)  # retorna a menor dessas datas

    def closest_date(stock):
        data_atual = datetime.now().strftime('%Y-%m-%d')
        data_mais_antiga = [
            data['data_de_validade']
            for data in stock
            if data['data_de_validade'] > data_atual
            # Retorna os elementos em que a data for maior que a data_atual
        ]
        return min(data_mais_antiga)  # retorna a menor dessas datas
