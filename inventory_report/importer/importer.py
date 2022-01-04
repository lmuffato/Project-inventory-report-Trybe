from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(file_to_read):
        raise NotImplementedError
