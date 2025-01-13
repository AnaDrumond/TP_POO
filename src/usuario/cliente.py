from usuario.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, senha: str) -> None:
        super().__init__(nome, senha)
        self.livros_reservados = []
        self.multa_total = 0 
    
    def exibir_painel(self) -> str:
        return "Painel do Cliente"

    def adicionar_livro_reservado(self, livro: dict) -> None:
        self.livros_reservados.append(livro)

    def remover_livro_reservado(self, livro: dict) -> None:
        if livro in self.livros_reservados:
            self.livros_reservados.remove(livro)

    def calcular_multa(self, livro: dict, dias_atraso: int) -> float:
        if dias_atraso > 0 and livro.get("reserva") and livro["reserva"].get("valor"):
            multa = livro["reserva"]["valor"] * dias_atraso
            self.multa_total += multa
            return multa
        return 0

    def get_multa_total(self) -> float:
        return self.multa_total

    def pagar_multas(self) -> None:
        self.multa_total = 0.0

    def get_livros_reservados(self) -> list:
        return self.livros_reservados
