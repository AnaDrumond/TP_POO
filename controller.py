from model import BibliotecaModel

class BibliotecaController:
    def __init__(self):
        self.biblioteca = BibliotecaModel()

    def add_book(self, livro):
        self.biblioteca.add_book(livro)

    def list_books(self):
        return self.biblioteca.list_books()

    def add_user(self, usuario):
        self.biblioteca.add_user(usuario)

    def list_users(self):
        return self.biblioteca.list_users()

    def add_loan(self, emprestimo):
        self.biblioteca.add_loan(emprestimo)

    def list_loans(self):
        return self.biblioteca.list_loans()
