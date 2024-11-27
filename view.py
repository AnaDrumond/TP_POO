from controller import BibliotecaController


# Instanciar o controlador
biblioteca = BibliotecaController()

# Inserir um novo livro
biblioteca.insert_book("Dom Quixote", "Miguel de Cervantes", "Editora A", 1605, "123456789")

# Inserir um novo usuário
biblioteca.insert_user("João", "Silva", "Rua Brasil, MG", "joao@gmail.com", "123456789")

# Realizar um empréstimo
biblioteca.insert_loan(1, 1, "2024-11-26")

# Exibir livros emprestados
livros_emprestados = biblioteca.get_books_on_loan()
if livros_emprestados:
    print("Livros emprestados:")
    for livro in livros_emprestados:
        print(f"Título: {livro['titulo']}")
        print(f"Usuário: {livro['usuario']}")
        print(f"Data de Empréstimo: {livro['data_emprestimo']}")
        print(f"Data de Devolução: {livro['data_devolucao']}")
        print("\n")
else:
    print("Nenhum livro emprestado no momento.")

# Atualizar a data de devolução de um empréstimo
biblioteca.update_loan_return_date(1, "2024-12-01")
