from abc import ABC, abstractmethod
import os


class Importer(ABC):
    @abstractmethod
    def import_data(fileName):
        raise NotImplementedError

    def get_file_informations(path):
        file_path_without_type, file_type = os.path.splitext(path)

        return {
            "file_name": file_path_without_type.split("/")[-1] + file_type,
            "file_type": file_type,
            "file_path": path,
        }
