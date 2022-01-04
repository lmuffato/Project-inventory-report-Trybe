from datetime import datetime


class CheckDate:
    @classmethod
    def filter_oldest(cls, array):
        '''Método da classe que filtra por data mais antiga'''
        dates = cls.__dates_to_datetime(array)
        oldest = cls.__oldest_date(dates)
        return oldest.strftime("%y/%m/%d")

    def __dates_to_datetime(array):
        '''Método privado para transformar um
        array de datas (string) em datetimes'''
        return [datetime.strptime(date, '%y/%m/%d') for date in array]

    def __oldest_date(array):
        oldest = array[0]
        for date in array:
            if oldest > date:
                oldest = date
        return oldest
