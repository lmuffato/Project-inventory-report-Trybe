from abc import abstractmethod


class Importer:
    @abstractmethod
    def import_data(self, file):
        pass
