from tkinter import *
from tkinter import ttk
from controller import BibliotecaController

# Inicializar o controlador
biblioteca = BibliotecaController()

# Criar a janela principal
janela = Tk()
janela.title("Biblioteca")
janela.geometry("800x600")
janela.configure(bg="#f0f0f0")

# Funções da interface
def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    editora = entry_editora.get()
    ano = entry_ano.get()
    isbn = entry_isbn.get()
    
    if titulo and autor and editora and ano and isbn:
        biblioteca.insert_book(titulo, autor, editora, int(ano), isbn)
        atualizar_lista_livros()
        limpar_campos()
    else:
        print("Preencha todos os campos!")

def atualizar_lista_livros():
    livros = biblioteca.list_books()
    tree_livros.delete(*tree_livros.get_children())
    for livro in livros:
        tree_livros.insert("", "end", values=livro)

def limpar_campos():
    entry_titulo.delete(0, END)
    entry_autor.delete(0, END)
    entry_editora.delete(0, END)
    entry_ano.delete(0, END)
    entry_isbn.delete(0, END)

# Criar Frames
frame_top = Frame(janela, bg="#6e8faf", height=50)
frame_top.pack(fill=X)

frame_form = Frame(janela, bg="#f0f0f0", padx=10, pady=10)
frame_form.pack(fill=X)

frame_table = Frame(janela, bg="#f0f0f0")
frame_table.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Widgets do Formulário
Label(frame_form, text="Título:", bg="#f0f0f0").grid(row=0, column=0, sticky=W, pady=5)
entry_titulo = Entry(frame_form, width=30)
entry_titulo.grid(row=0, column=1, pady=5)

Label(frame_form, text="Autor:", bg="#f0f0f0").grid(row=1, column=0, sticky=W, pady=5)
entry_autor = Entry(frame_form, width=30)
entry_autor.grid(row=1, column=1, pady=5)

Label(frame_form, text="Editora:", bg="#f0f0f0").grid(row=2, column=0, sticky=W, pady=5)
entry_editora = Entry(frame_form, width=30)
entry_editora.grid(row=2, column=1, pady=5)

Label(frame_form, text="Ano de Publicação:", bg="#f0f0f0").grid(row=3, column=0, sticky=W, pady=5)
entry_ano = Entry(frame_form, width=30)
entry_ano.grid(row=3, column=1, pady=5)

Label(frame_form, text="ISBN:", bg="#f0f0f0").grid(row=4, column=0, sticky=W, pady=5)
entry_isbn = Entry(frame_form, width=30)
entry_isbn.grid(row=4, column=1, pady=5)

Button(frame_form, text="Adicionar Livro", command=adicionar_livro, bg="#6e8faf", fg="white").grid(row=5, columnspan=2, pady=10)

# Tabela de Livros
tree_livros = ttk.Treeview(frame_table, columns=("ID", "Título", "Autor", "Editora", "Ano", "ISBN"), show="headings")
tree_livros.heading("ID", text="ID")
tree_livros.heading("Título", text="Título")
tree_livros.heading("Autor", text="Autor")
tree_livros.heading("Editora", text="Editora")
tree_livros.heading("Ano", text="Ano")
tree_livros.heading("ISBN", text="ISBN")
tree_livros.pack(fill=BOTH, expand=True)

# Atualizar tabela inicial
atualizar_lista_livros()

# Iniciar o loop da janela
janela.mainloop()
