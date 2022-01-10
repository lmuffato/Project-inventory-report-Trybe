# Feito por Renan Oliveira
from datetime import datetime


class CheckDate:
    @classmethod
    def filter_oldest(cls, array):
        '''Método da classe que filtra por data mais antiga'''
        dates = cls.__dates_to_datetime(array)
        oldest = cls.__oldest_date(dates)
        oldest_str = oldest.strftime('%Y-%m-%d')
        return oldest_str

    @classmethod
    def filter_closest(cls, array):
        '''Método da classe que filtra por data mais próxima da atual'''
        dates = cls.__dates_to_datetime(array)
        closest = cls.__closest_date(dates)
        closest_str = closest.strftime('%Y-%m-%d')
        return closest_str

    def __dates_to_datetime(array):
        '''Método privado para transformar um
        array de datas (string) em datetimes'''
        return [datetime.strptime(date, '%Y-%m-%d') for date in array]

    def __oldest_date(array):
        oldest = array[0]
        for date in array:
            if oldest > date:
                oldest = date
        return oldest

    def __closest_date(array):
        '''Método privado que retorna a data mais
        próxima da data atual - inspirado na solução proposta em
        www.geeksforgeeks.org/python-find-the-closest-date-from-a-list/'''
        now = datetime.now()
        dates_dict = {
            abs(now.timestamp() - date.timestamp()): date
            for date in array
        }
        closest = dates_dict[min(dates_dict.keys())]
        return closest
