import tkinter as tk
from controllers.auth_controller import AuthController

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")

        tk.Label(self.root, text="Usuário:").pack()
        self.entrada_usuario = tk.Entry(self.root)
        self.entrada_usuario.pack()

        tk.Label(self.root, text="Senha:").pack()
        self.entrada_senha = tk.Entry(self.root, show="*")
        self.entrada_senha.pack()

        tk.Button(self.root, text="Login", command=self.fazer_login).pack()
        tk.Button(self.root, text="Cadastrar", command=self.abrir_tela_cadastro).pack()

    def fazer_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        tipo_usuario = AuthController.login(usuario, senha)

        if tipo_usuario == "cliente":
            self.abrir_tela_cliente()
        elif tipo_usuario == "administrador":
            self.abrir_tela_administrador()

    def abrir_tela_cadastro(self):
        tela_cadastro = tk.Toplevel(self.root)
        tela_cadastro.title("Cadastro de Usuário")

        tk.Label(tela_cadastro, text="Usuário:").pack()
        entrada_usuario = tk.Entry(tela_cadastro)
        entrada_usuario.pack()

        tk.Label(tela_cadastro, text="Senha:").pack()
        entrada_senha = tk.Entry(tela_cadastro, show="*")
        entrada_senha.pack()

        tk.Label(tela_cadastro, text="Confirme a senha:").pack()
        entrada_confirmacao = tk.Entry(tela_cadastro, show="*")
        entrada_confirmacao.pack()

        tk.Label(tela_cadastro, text="Tipo de Usuário:").pack()
        tipo_usuario = tk.StringVar(value="cliente")
        tk.Radiobutton(tela_cadastro, text="Cliente", variable=tipo_usuario, value="cliente").pack()
        tk.Radiobutton(tela_cadastro, text="Administrador", variable=tipo_usuario, value="administrador").pack()

        def cadastrar():
            usuario = entrada_usuario.get()
            senha = entrada_senha.get()
            confirmacao = entrada_confirmacao.get()
            tipo = tipo_usuario.get()
            AuthController.cadastrar(usuario, senha, confirmacao, tipo)

        tk.Button(tela_cadastro, text="Cadastrar", command=cadastrar).pack()

    def abrir_tela_cliente(self):
        tela_cliente = tk.Toplevel(self.root)
        tela_cliente.title("Área do Cliente")
        tk.Label(tela_cliente, text="Bem-vindo, Cliente!").pack()

    def abrir_tela_administrador(self):
        tela_administrador = tk.Toplevel(self.root)
        tela_administrador.title("Área do Administrador")
        tk.Label(tela_administrador, text="Bem-vindo, Administrador!").pack()
