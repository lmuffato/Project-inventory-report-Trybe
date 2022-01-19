from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod  # decorador que indica o método abstrato
    def import_data(path):
        pass  # deixa que as ações da função seja feita por outra classe

# O @abstractmethod vs classmethod

# @abstractmethod:
# Use apenas os recursos da própria função.

# @classmethod
# Utiliza outros recursos da classe, precisando do cls para
# invoca-los no lugar do self.

# Obs.: desde a versão 3.3: agora é possível usar
# @classmethod com o abstractmethod, tornando este decorador redundante.
