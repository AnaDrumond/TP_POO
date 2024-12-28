import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from interface.tela_administrador import TelaAdministrador
from interface.tela_cliente import TelaCliente
from interface.tela_cadastro import TelaCadastro
from usuario.cliente import Cliente
from usuario.administrador import Administrador

class TelaLogin:
    def __init__(self, sistema: Sistema):
        self.sistema = sistema

        self.root = tk.Tk()
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("400x300")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Usuário:").grid(row=0, column=0, pady=5, sticky="w")
        self.nome_entry = tk.Entry(frame, width=30)
        self.nome_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Senha:").grid(row=1, column=0, pady=5, sticky="w")
        self.senha_entry = tk.Entry(frame, show="*", width=30)
        self.senha_entry.grid(row=1, column=1, pady=5)

        tk.Button(frame, text="Login", command=self.login, width=15).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="Cadastrar", command=self.cadastrar, width=15).grid(row=2, column=1, pady=10)

        self.root.mainloop()

    def login(self):
        nome = self.nome_entry.get()
        senha = self.senha_entry.get()

        try:
            usuario = self.sistema.autenticar_usuario(nome, senha)
            if isinstance(usuario, Cliente):
                TelaCliente(self.sistema)
            elif isinstance(usuario, Administrador):
                TelaAdministrador(self.sistema)

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def cadastrar(self):
        TelaCadastro(self.sistema)
