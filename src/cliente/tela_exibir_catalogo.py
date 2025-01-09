import tkinter as tk
from tkinter import ttk
from sistema.sistema import Sistema
import sys

if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)

class TelaExibirCatalogo:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Toplevel()
        self.root.title("Catálogo de Livros")
        self.root.geometry("600x400")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Catálogo de Livros", font=("Arial", 14, "bold")).pack(pady=10)

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

        tk.Button(frame, text="Fechar", command=self.root.destroy, width=15).pack(pady=10)

        self.carregar_livros()

    def carregar_livros(self) -> None:
        for i, livro in enumerate(self.sistema.livros, start=1):
            print(f"Título no JSON: {livro['titulo']}")
            self.tree.insert(
                "", "end",
                values=(
                    i,
                    livro['titulo'],  
                    livro['autor'],
                    livro['ano'],
                    "Sim" if livro.get('disponivel', True) else "Não"
                )
            )
