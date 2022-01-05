from datetime import datetime


class CheckDate:
    @classmethod
    def filter_oldest(cls, array):
        '''Método da classe que filtra por data mais antiga'''
        # print('FILTER OLDEST CALLED', array)
        dates = cls.__dates_to_datetime(array)
        # print('DATETIMES', dates)
        oldest = cls.__oldest_date(dates)
        # print('OLDEST', oldest)
        oldest_str = oldest.strftime('%Y-%m-%d')
        print('OLDEST STR', oldest_str)
        return oldest_str

    def __dates_to_datetime(array):
        '''Método privado para transformar um
        array de datas (string) em datetimes'''
        return [datetime.strptime(date, '%Y-%m-%d') for date in array]
        # return [date for date in array]

    def __oldest_date(array):
        oldest = array[0]
        for date in array:
            if oldest > date:
                oldest = date
        return oldest
