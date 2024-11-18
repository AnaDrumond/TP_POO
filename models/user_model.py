import os
import hashlib

class UserModel:
    # Defina o caminho para o arquivo .txt dentro da pasta database
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "../database/usuarios.txt")

    @staticmethod
    def inicializar_arquivo():
        # Crie a pasta 'database' se ela não existir
        pasta_database = os.path.dirname(UserModel.caminho_arquivo)
        if not os.path.exists(pasta_database):
            os.makedirs(pasta_database)

        # Crie o arquivo 'usuarios.txt' se ele não existir
        if not os.path.exists(UserModel.caminho_arquivo):
            with open(UserModel.caminho_arquivo, "w") as arquivo:
                pass  # Apenas cria o arquivo vazio

    @staticmethod
    def cadastrar_usuario(usuario, senha, tipo="cliente"):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        with open(UserModel.caminho_arquivo, "a") as arquivo:
            arquivo.write(f"{usuario},{senha_hash},{tipo}\n")
        return True

    @staticmethod
    def validar_login(usuario, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        try:
            with open(UserModel.caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    usuario_arquivo, senha_arquivo, tipo_arquivo = linha.strip().split(",")
                    if usuario_arquivo == usuario and senha_arquivo == senha_hash:
                        return tipo_arquivo
        except FileNotFoundError:
            return None
        return None
