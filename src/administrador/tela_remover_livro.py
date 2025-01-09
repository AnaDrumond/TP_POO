import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.administrador import Administrador

class TelaRemoverLivro:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Toplevel()
        self.root.title("Remover Livro")
        self.root.geometry("400x300")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Selecione o Livro para Remover:").grid(row=0, column=0, pady=5, sticky="w")
        self.livro_var = tk.StringVar(value="")
        livros_opcoes = [f"{livro['titulo']} - {livro['autor']} ({livro['ano']})" for livro in self.sistema.livros]
        self.livro_menu = tk.OptionMenu(frame, self.livro_var, *livros_opcoes)
        self.livro_menu.grid(row=0, column=1, pady=5)

        tk.Button(frame, text="Remover Livro", command=self.remover_livro, width=20).grid(row=1, columnspan=2, pady=10)

    def remover_livro(self) -> None:
        livro_selecionado = self.livro_var.get()

        if not livro_selecionado:
            messagebox.showerror("Erro", "Nenhum livro selecionado.")
            return

        titulo = livro_selecionado.split(" - ")[0]  # Extrai o título original

        try:
            self.sistema.remover_livro(titulo)
            messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))