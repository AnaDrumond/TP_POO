from usuario.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome: str, senha: str) -> None:
        super().__init__(nome, senha)

    def exibir_painel(self) -> str:
        return "Painel do Administrador"