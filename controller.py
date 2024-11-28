from model import BibliotecaModel

class BibliotecaController:
    def __init__(self):
        self.biblioteca = BibliotecaModel()

    # Adiciona um novo livro, recebendo os detalhes como parâmetros separados
    def add_book(self, titulo, autor, genero, ano):
        livro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "ano": ano
        }
        self.biblioteca.add_book(livro)

    # Lista todos os livros armazenados
    def list_books(self):
        return self.biblioteca.list_books()

    # Adiciona um novo usuário, recebendo os detalhes como parâmetros separados
    def add_user(self, nome, sobrenome, endereco, email, telefone):
        usuario = {
            "nome": nome,
            "sobrenome": sobrenome,
            "endereco": endereco,
            "email": email,
            "telefone": telefone
        }
        self.biblioteca.add_user(usuario)

    # Lista todos os usuários cadastrados
    def list_users(self):
        return self.biblioteca.list_users()

    # Adiciona um empréstimo de livro, recebendo um dicionário com os detalhes
    def add_loan(self, usuario_id, livro_id, data_emprestimo, data_devolucao):
        emprestimo = {
            "usuario_id": usuario_id,
            "livro_id": livro_id,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao
        }
        self.biblioteca.add_loan(emprestimo)

    # Lista todos os empréstimos realizados
    def list_loans(self):
        return self.biblioteca.list_loans()
