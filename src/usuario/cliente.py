from usuario.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, senha: str) -> None:
        super().__init__(nome, senha)
        self.livros_reservados = []  # Lista de livros reservados
        self.multa_total = 0  # Campo para armazenar a multa total
    
    def exibir_painel(self) -> str:
        return "Painel do Cliente"

    # Método para adicionar um livro à lista de livros reservados
    def adicionar_livro_reservado(self, livro: dict) -> None:
        self.livros_reservados.append(livro)

    # Método para remover um livro da lista de livros reservados
    def remover_livro_reservado(self, livro: dict) -> None:
        if livro in self.livros_reservados:
            self.livros_reservados.remove(livro)

    # Método para calcular a multa
    def calcular_multa(self, livro: dict, dias_atraso: int) -> float:
        if dias_atraso > 0 and livro.get("reserva") and livro["reserva"].get("valor"):
            multa = livro["reserva"]["valor"] * dias_atraso  # A multa é calculada pelo valor por dia de atraso
            self.multa_total += multa
            return multa
        return 0

    # Método para obter a multa total do cliente
    def get_multa_total(self) -> float:
        return self.multa_total

    # Método para zerar as multas após o pagamento
    def pagar_multas(self) -> None:
        """
        Reseta a multa total para 0, indicando que o cliente pagou todas as suas multas.
        """
        self.multa_total = 0.0

    # Método para obter a lista de livros reservados
    def get_livros_reservados(self) -> list:
        return self.livros_reservados
