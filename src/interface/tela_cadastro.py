import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente
from usuario.administrador import Administrador

class TelaCadastro:
    def __init__(self, sistema: Sistema) -> None:
        self.sistema = sistema

        self.root = tk.Toplevel()
        self.root.title("Cadastro")
        self.root.geometry("400x400")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, pady=5, sticky="w")
        self.nome_entry = tk.Entry(frame, width=30)
        self.nome_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Email:").grid(row=1, column=0, pady=5, sticky="w")
        self.email_entry = tk.Entry(frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Senha:").grid(row=2, column=0, pady=5, sticky="w")
        self.senha_entry = tk.Entry(frame, show="*", width=30)
        self.senha_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Confirmar Senha:").grid(row=3, column=0, pady=5, sticky="w")
        self.confirmar_senha_entry = tk.Entry(frame, show="*", width=30)
        self.confirmar_senha_entry.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Tipo de Usuário:").grid(row=4, column=0, pady=5, sticky="w")
        self.tipo_var = tk.StringVar(value="cliente")
        tk.Radiobutton(frame, text="Cliente", variable=self.tipo_var, value="cliente").grid(row=4, column=1, pady=5, sticky="w")
        tk.Radiobutton(frame, text="Administrador", variable=self.tipo_var, value="administrador").grid(row=5, column=1, pady=5, sticky="w")

        tk.Button(frame, text="Cadastrar", command=self.cadastrar, width=20).grid(row=6, columnspan=2, pady=10)

    def cadastrar(self) -> None:
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        confirmar_senha = self.confirmar_senha_entry.get()
        tipo = self.tipo_var.get()

        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        try:
            self.sistema.cadastrar_usuario(nome, email, senha, tipo)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
