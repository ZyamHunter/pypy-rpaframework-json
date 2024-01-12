import shutil
import tempfile
import os
from RPA.Tables import Tables

class TableOperations:
    @staticmethod
    def load_table_from_file(file_path):
        table_file_path = os.path.abspath(file_path)
        """
        Carrega uma TABELA de um arquivo.
        """
        with open(table_file_path, "r", encoding="utf-8") as file:
            data = file.read()
            return table_file_path
