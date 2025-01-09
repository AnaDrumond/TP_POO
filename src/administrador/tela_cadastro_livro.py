import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.administrador import Administrador

class TelaCadastroLivro:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Toplevel()
        self.root.title("Cadastrar Novo Livro")
        self.root.geometry("400x300")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Título:").grid(row=0, column=0, pady=5, sticky="w")
        self.titulo_entry = tk.Entry(frame, width=30)
        self.titulo_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Autor:").grid(row=1, column=0, pady=5, sticky="w")
        self.autor_entry = tk.Entry(frame, width=30)
        self.autor_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Ano:").grid(row=2, column=0, pady=5, sticky="w")
        self.ano_entry = tk.Entry(frame, width=30)
        self.ano_entry.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Cadastrar", command=self.cadastrar_livro, width=20).grid(row=3, columnspan=2, pady=10)

    def cadastrar_livro(self) -> None:
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()

        if not titulo or not autor or not ano.isdigit():
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return

        try:
            self.sistema.cadastrar_livro(titulo, autor, int(ano))
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))