from models.user_model import UserModel
from tkinter import messagebox

class AuthController:
    @staticmethod
    def cadastrar(usuario, senha, confirmacao, tipo):
        if not usuario or not senha:
            messagebox.showerror("Erro", "Usuário e senha não podem estar vazios.")
            return False

        if senha != confirmacao:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return False

        UserModel.cadastrar_usuario(usuario, senha, tipo)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        return True

    @staticmethod
    def login(usuario, senha):
        tipo_usuario = UserModel.validar_login(usuario, senha)
        if tipo_usuario:
            messagebox.showinfo("Sucesso", f"Login realizado com sucesso! Tipo de usuário: {tipo_usuario.capitalize()}")
            return tipo_usuario
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            return None
