import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.administrador import Administrador

class TelaExibirLivros:
    def __init__(self, sistema):
        self.sistema = sistema

        # Criação da janela principal
        self.root = tk.Toplevel()
        self.root.title("Exibir Todos os Livros")
        self.root.geometry("600x400")

        # Configuração do layout
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        # Título
        tk.Label(frame, text="Todos os livros do banco de dados", font=("Arial", 14, "bold")).pack(pady=10)

        # Tabela para exibir os livros
        self.tree = ttk.Treeview(frame, columns=("ID", "Título", "Autor", "Ano", "Disponível"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Ano", text="Ano")
        self.tree.heading("Disponível", text="Disponível")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Título", width=200, anchor="w")
        self.tree.column("Autor", width=150, anchor="w")
        self.tree.column("Ano", width=80, anchor="center")
        self.tree.column("Disponível", width=80, anchor="center")

        self.tree.pack(expand=True, fill="both", pady=10)

        # Botão para fechar a janela
        tk.Button(frame, text="Fechar", command=self.root.destroy, width=15).pack(pady=10)

        # Carregar os livros na tabela
        self.carregar_livros()

    def carregar_livros(self):
        """Carrega os livros na tabela."""
        for i, livro in enumerate(self.sistema.livros, start=1):
            self.tree.insert("", "end", values=(i, livro['titulo'], livro['autor'], livro['ano'], "Sim" if livro.get('disponivel', True) else "Não"))
