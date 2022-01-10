# para o melhor entendimento dos requisitos e vizualizacao dos codigos,
# fiz uma pesquisa dentre varios projetos de colegas da turma.
# Feito por minha dupla Nathalia Zebral
from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(file_path):
        raise NotImplementedError
