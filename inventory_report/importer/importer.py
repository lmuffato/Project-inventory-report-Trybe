# essa é a sintaxe para criação de uma clase abstrata Importer
# como se ela fosse herdeira da classe ABC
# sintaxe está no course em 33.2 - Herança - Especialização de
# comportamentos
# @abstractmethod para indicar que o método import_data
# deverá ser implementado de acordo com as regras de negócio
# das classes herdeiras da classe mãe Importer

from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(file_to_read):
        raise NotImplementedError
