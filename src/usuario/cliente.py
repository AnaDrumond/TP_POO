from usuario.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, senha: str):
        super().__init__(nome, senha)

    def exibir_painel(self):
        return "Painel do Cliente"