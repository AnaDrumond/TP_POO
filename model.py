import json

class BibliotecaModel:
    def __init__(self):
        self.arquivo_biblioteca = "biblioteca.json"
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo_biblioteca, "r") as arquivo:
                self.dados = json.load(arquivo)
        except FileNotFoundError:
            self.dados = {"livros": [], "usuarios": [], "emprestimos": []}

    def salvar_dados(self):
        with open(self.arquivo_biblioteca, "w") as arquivo:
            json.dump(self.dados, arquivo, indent=4)

    def add_book(self, livro):
        self.dados["livros"].append(livro)
        self.salvar_dados()

    def list_books(self):
        return self.dados["livros"]

    def add_user(self, usuario):
        self.dados["usuarios"].append(usuario)
        self.salvar_dados()

    def list_users(self):
        return self.dados["usuarios"]

    def add_loan(self, emprestimo):
        self.dados["emprestimos"].append(emprestimo)
        self.salvar_dados()

    def list_loans(self):
        return self.dados["emprestimos"]
