from usuario.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, senha: str):
        super().__init__(nome, senha)
        self.livros_reservados = []  # Lista de livros reservados
        self.multa_total = 0  # Campo para armazenar a multa total
    
    def exibir_painel(self):
        return "Painel do Cliente"

# Método para adicionar um livro à lista de livros reservados
    def adicionar_livro_reservado(self, livro):
        self.livros_reservados.append(livro)

    # Método para remover um livro da lista de livros reservados
    def remover_livro_reservado(self, livro):
        if livro in self.livros_reservados:
            self.livros_reservados.remove(livro)

    # Método para calcular a multa
    def calcular_multa(self, livro, dias_atraso):
        if dias_atraso > 0 and livro.get("multa"):
            multa = livro["multa"] * dias_atraso  # A multa é calculada pelo valor por dia de atraso
            self.multa_total += multa
            return multa
        return 0

    # Método para obter a multa total do cliente
    def get_multa_total(self):
        return self.multa_total

    # Método para obter a lista de livros reservados
    def get_livros_reservados(self):
        return self.livros_reservados
