from abc import ABC, abstractmethod
from statistics import mode


class Report(ABC):
    @abstractmethod
    def generate(cls, data):
        raise NotImplementedError

    def filter_company(data):
        most_frequent = mode(data)
        print(most_frequent)
        return most_frequent
