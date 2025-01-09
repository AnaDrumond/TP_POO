import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.administrador import Administrador

class TelaEditarLivro:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Toplevel()
        self.root.title("Editar Livro")
        self.root.geometry("400x400")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Selecione o Livro:").grid(row=0, column=0, pady=5, sticky="w")
        self.livro_var = tk.StringVar(value="")
        livros_opcoes = [f"{livro['titulo']} - {livro['autor']} ({livro['ano']})" for livro in self.sistema.livros]
        self.livro_menu = tk.OptionMenu(frame, self.livro_var, *livros_opcoes)
        self.livro_menu.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Novo Título:").grid(row=1, column=0, pady=5, sticky="w")
        self.titulo_entry = tk.Entry(frame, width=30)
        self.titulo_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Novo Autor:").grid(row=2, column=0, pady=5, sticky="w")
        self.autor_entry = tk.Entry(frame, width=30)
        self.autor_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Novo Ano:").grid(row=3, column=0, pady=5, sticky="w")
        self.ano_entry = tk.Entry(frame, width=30)
        self.ano_entry.grid(row=3, column=1, pady=5)

        tk.Button(frame, text="Salvar Alterações", command=self.editar_livro, width=20).grid(row=4, columnspan=2, pady=10)

    def editar_livro(self) -> None:
        livro_selecionado = self.livro_var.get()
        novo_titulo = self.titulo_entry.get()
        novo_autor = self.autor_entry.get()
        novo_ano = self.ano_entry.get()

        if not livro_selecionado:
            messagebox.showerror("Erro", "Nenhum livro selecionado.")
            return

        if not novo_titulo or not novo_autor or not novo_ano.isdigit():
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return

        titulo_atual = livro_selecionado.split(" - ")[0]  # Extrai o título original

        try:
            self.sistema.editar_livro(titulo_atual, novo_titulo, novo_autor, int(novo_ano))
            messagebox.showinfo("Sucesso", "Livro editado com sucesso!")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
