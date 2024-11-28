import tkinter as tk
from tkinter import ttk, messagebox
from controller import BibliotecaController


biblioteca = BibliotecaController()


def atualizar_lista_usuarios():
    tree_usuarios.delete(*tree_usuarios.get_children())
    usuarios = biblioteca.list_users()
    for usuario in usuarios:
        tree_usuarios.insert("", "end", values=(usuario["id"], usuario["nome"], usuario["sobrenome"], usuario["endereco"], usuario["email"], usuario["telefone"]))


def novo_usuario():
    def salvar_usuario():
        nome = entry_nome.get()
        sobrenome = entry_sobrenome.get()
        endereco = entry_endereco.get()
        email = entry_email.get()
        telefone = entry_telefone.get()

        if nome and sobrenome and email:
            biblioteca.add_user(nome, sobrenome, endereco, email, telefone)
            atualizar_lista_usuarios()
            janela.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser preenchidos!")

    janela = tk.Toplevel(root)
    janela.title("Novo Usuário")

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela, text="Sobrenome:").grid(row=1, column=0, padx=10, pady=5)
    entry_sobrenome = tk.Entry(janela)
    entry_sobrenome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela, text="Endereço:").grid(row=2, column=0, padx=10, pady=5)
    entry_endereco = tk.Entry(janela)
    entry_endereco.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela, text="E-mail:").grid(row=3, column=0, padx=10, pady=5)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(janela, text="Telefone:").grid(row=4, column=0, padx=10, pady=5)
    entry_telefone = tk.Entry(janela)
    entry_telefone.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(janela, text="Salvar", command=salvar_usuario).grid(row=5, columnspan=2, pady=10)


def novo_livro():
    def salvar_livro():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        genero = entry_genero.get()
        ano = entry_ano.get()

        if titulo and autor and genero:
            biblioteca.add_book(titulo, autor, genero, ano)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            janela.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser preenchidos!")

    janela = tk.Toplevel(root)
    janela.title("Novo Livro")

    tk.Label(janela, text="Título:").grid(row=0, column=0, padx=10, pady=5)
    entry_titulo = tk.Entry(janela)
    entry_titulo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
    entry_autor = tk.Entry(janela)
    entry_autor.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela, text="Gênero:").grid(row=2, column=0, padx=10, pady=5)
    entry_genero = tk.Entry(janela)
    entry_genero.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela, text="Ano:").grid(row=3, column=0, padx=10, pady=5)
    entry_ano = tk.Entry(janela)
    entry_ano.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(janela, text="Salvar", command=salvar_livro).grid(row=4, columnspan=2, pady=10)


root = tk.Tk()
root.title("Sistema de Gerenciamento de Livros")
root.geometry("800x600")


frame_lateral = tk.Frame(root, bg="lightgray", width=200)
frame_lateral.pack(side="left", fill="y")

tk.Label(frame_lateral, text="Sistema de Gerenciamento de Livros", bg="lightgray", font=("Arial", 14, "bold"), wraplength=180).pack(pady=20)
tk.Button(frame_lateral, text="Novo usuário", command=novo_usuario).pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Novo livro", command=novo_livro).pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Exibir todos os livros").pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Exibir todos os usuários", command=atualizar_lista_usuarios).pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Realizar um empréstimo").pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Devolução de um empréstimo").pack(fill="x", pady=5)
tk.Button(frame_lateral, text="Livros emprestados no momento").pack(fill="x", pady=5)


frame_principal = tk.Frame(root)
frame_principal.pack(side="right", fill="both", expand=True)

tk.Label(frame_principal, text="Todos os usuários do banco de dados", font=("Arial", 12, "bold")).pack(pady=10)


colunas = ("ID", "Nome", "Sobrenome", "Endereço", "Email", "Telefone")
tree_usuarios = ttk.Treeview(frame_principal, columns=colunas, show="headings")

for coluna in colunas:
    tree_usuarios.heading(coluna, text=coluna)
    tree_usuarios.column(coluna, width=120, anchor="center")

tree_usuarios.pack(fill="both", expand=True)


atualizar_lista_usuarios()


root.mainloop()
