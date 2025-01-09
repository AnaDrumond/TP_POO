import tkinter as tk
from tkinter import messagebox, ttk
from sistema.sistema import Sistema
from usuario.administrador import Administrador
from administrador.tela_cadastro_livro import TelaCadastroLivro
from administrador.tela_editar_livro import TelaEditarLivro
from administrador.tela_remover_livro import TelaRemoverLivro
from administrador.tela_exibir_livros import TelaExibirLivros

class TelaAdministrador:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Tk()
        self.root.title("Painel do Administrador")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Bem-vindo ao Painel do Administrador!", font=("Arial", 14, "bold"), wraplength=180).pack(pady=20)

        tk.Button(self.root, text="Ver Catálogo de Livros", command=self.ver_catalogo, width=30).pack(pady=5)
        tk.Button(self.root, text="Cadastrar Novo Livro", command=self.novo_livro, width=30).pack(pady=5)
        tk.Button(self.root, text="Editar Livro", command=self.editar_livro, width=30).pack(pady=5)
        tk.Button(self.root, text="Remover Livro", command=self.remover_livro, width=30).pack(pady=5)

    def ver_catalogo(self) -> None:
        janela_livros = tk.Toplevel(self.root)
        janela_livros.title("Catálogo de Livros")
        janela_livros.geometry("700x400")

        frame = tk.Frame(janela_livros, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Catálogo de Livros", font=("Arial", 14, "bold")).pack(pady=10)

        tree = ttk.Treeview(frame, columns=("ID", "Título", "Autor", "Ano", "Disponível"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")
        tree.heading("Ano", text="Ano")
        tree.heading("Disponível", text="Disponível")

        tree.column("ID", width=50, anchor="center")
        tree.column("Título", width=250, anchor="w")
        tree.column("Autor", width=150, anchor="w")
        tree.column("Ano", width=100, anchor="center")
        tree.column("Disponível", width=100, anchor="center")

        tree.pack(expand=True, fill="both", pady=10)

        tk.Button(frame, text="Fechar", command=janela_livros.destroy, width=15).pack(pady=10)

        self.carregar_livros_na_tabela(tree)

    def carregar_livros_na_tabela(self, tree) -> None:
        """Carrega os livros na tabela."""
        for i, livro in enumerate(self.sistema.livros, start=1):
            tree.insert("", "end", values=(
                i,
                livro["titulo"],
                livro["autor"],
                livro["ano"],
                "Sim" if livro.get("disponivel", True) else "Não"
            ))


    def novo_livro(self) -> None:
        TelaCadastroLivro(self.sistema)

    def editar_livro(self) -> None:
        TelaEditarLivro(self.sistema)

    def remover_livro(self) -> None:
        TelaRemoverLivro(self.sistema)

