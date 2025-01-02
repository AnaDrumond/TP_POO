import tkinter as tk
from tkinter import ttk
import json
import os
import hashlib
import datetime
from usuario.cliente import Cliente
from usuario.administrador import Administrador

class Sistema:
    def __init__(self, arquivo_dados="usuarios.json", arquivo_livros="livros.json"):
        self.arquivo_dados = arquivo_dados
        self.arquivo_livros = arquivo_livros

        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'database'))
        
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
        self.arquivo_dados = os.path.join(self.base_dir, arquivo_dados)
        self.arquivo_livros = os.path.join(self.base_dir, arquivo_livros)
        
        self.carregar_dados()
        self.carregar_livros()

    def carregar_dados(self):
        try:
            with open(self.arquivo_dados, 'r') as arquivo:
                self.usuarios = json.load(arquivo)
        except FileNotFoundError:
            self.usuarios = []

    def salvar_dados(self):
        with open(self.arquivo_dados, 'w') as arquivo:
            json.dump(self.usuarios, arquivo, indent=4)

    def carregar_livros(self):
        try:
            with open(self.arquivo_livros, 'r') as arquivo:
                self.livros = json.load(arquivo)
        except FileNotFoundError:
            self.livros = []

    def salvar_livros(self):
        with open(self.arquivo_livros, 'w') as arquivo:
            json.dump(self.livros, arquivo, indent=4)

    def cadastrar_usuario(self, nome: str, email: str, senha: str, tipo: str):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        if not nome.isalpha():
            raise ValueError("O nome deve conter apenas letras.")

        if any(usuario['nome'] == nome for usuario in self.usuarios):
            raise ValueError("O nome de usuário já existe.")

        if any(usuario['email'] == email for usuario in self.usuarios):
            raise ValueError("O email já está cadastrado.")

        self.usuarios.append({"nome": nome, "email": email, "senha": senha_hash, "tipo": tipo})
        self.salvar_dados()

    def autenticar_usuario(self, nome: str, senha: str):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        for usuario in self.usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha_hash:
                if usuario['tipo'] == 'cliente':
                    return Cliente(nome, senha)
                elif usuario['tipo'] == 'administrador':
                    return Administrador(nome, senha)
        raise ValueError("Nome ou senha incorretos.")
    
    def cadastrar_livro(self, titulo: str, autor: str, ano: int):
        if any(livro['titulo'] == titulo for livro in self.livros):
            raise ValueError("Já existe um livro com esse título.")

        self.livros.append({"titulo": titulo, "autor": autor, "ano": ano})
        self.salvar_livros()

    def editar_livro(self, titulo_atual: str, novo_titulo: str, novo_autor: str, novo_ano: int):
        if not novo_titulo or not novo_autor or novo_ano <= 0:
            raise ValueError("Informações inválidas para o livro.")

        for livro in self.livros:
            if livro['titulo'] == titulo_atual:
                livro.update({"titulo": novo_titulo, "autor": novo_autor, "ano": novo_ano})
                self.salvar_livros()
                return
        raise ValueError("Livro não encontrado.")

    def remover_livro(self, titulo: str):
        livro_removido = next((livro for livro in self.livros if livro['titulo'] == titulo), None)
        if not livro_removido:
            raise ValueError("Livro não encontrado.")
        self.livros = [livro for livro in self.livros if livro['titulo'] != titulo]
        self.salvar_livros()
        return livro_removido
    
    def reservar_livro(self, titulo_livro, cliente, periodo): #Função para a reserva de livro do cliente;
        livro = next((l for l in self.livros if l["titulo"] == titulo_livro), None)
        if not livro:
            raise ValueError("Livro não encontrado.")
        if not livro.get("disponivel", True):
            raise ValueError("Livro indisponível para reserva.")

        valores_periodo = {5: 10.0, 10: 20.00} #Definição do período de empréstimo e seu valor;  
        valor = valores_periodo.get(periodo, None)
        if valor is None:
            raise ValueError("Período de empréstimo inválido.")
    
        for l in self.livros:
            if l["titulo"] == titulo_livro:
                l["disponivel"] = False
                l["reserva"] = {
                    "cliente": cliente.nome,
                    "periodo": periodo,
                    "valor": valor
                }
                break

    # Salvando as alterações no arquivo
        try:
            self.salvar_livros()
        except Exception as e:
            raise IOError(f"Erro ao salvar a reserva no arquivo: {str(e)}")

        return valor

