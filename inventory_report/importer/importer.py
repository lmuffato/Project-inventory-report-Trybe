from abc import ABC, abstractmethod
# https://docs.python.org/3/library/abc.html


class Importer(ABC):
    @abstractmethod
    def import_data(path):
        pass
