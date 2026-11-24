from abc import ABC, abstractmethod
import sqlite3
from pathlib import Path

class DAO(ABC):
    
    def __init__(self):
        self._conn = None
        self._nome_bd = str(Path(__file__).resolve().parent.parent / "agenda.db")

    def abrir(self):
        self._conn = sqlite3.connect(self._nome_bd)
        self._conn.execute("PRAGMA foreign_keys = ON")
 
    def fechar(self):
        if self._conn != None:
            self._conn.close()
            self._conn = None
       
    def execute(self, sql, params = None):
        cursor = self._conn.cursor()
        cursor.execute(sql, params or [])
        self._conn.commit()
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass