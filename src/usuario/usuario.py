from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, senha: str):
        self._nome = nome
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha

    @abstractmethod
    def exibir_painel(self):
        pass