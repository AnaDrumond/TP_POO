from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, senha: str) -> None:
        self._nome = nome
        self._senha = senha

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def senha(self) -> str:
        return self._senha

    @abstractmethod
    def exibir_painel(self) -> str:
        pass