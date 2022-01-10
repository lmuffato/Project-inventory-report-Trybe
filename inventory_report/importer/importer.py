from abc import abstractmethod


class Importer:
    @abstractmethod
    def import_data(path):
        raise NotImplementedError
