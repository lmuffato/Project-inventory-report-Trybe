from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, import_file):
        self.import_file = import_file

    @abstractmethod
    def import_data(self):
        raise NotImplementedError
