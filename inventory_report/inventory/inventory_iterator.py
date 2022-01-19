from collections.abc import Iterator


class InventoryIterator(Iterator):  # re-implementação da classe Iterator
    def __init__(self, data):   # construtor (parametros)
        self.data = data   # definindo atributo interno da classe
        self.counter = 0   # contagem inicial

    def __next__(self):    # o next do iterator, que repete a cada iteração
        try:
            current = self.data[self.counter]  # preenchendo o array
        except IndexError:
            raise StopIteration  # tratamento especifico do erro StopIteration
        else:
            self.counter += 1  # contador
            return current
