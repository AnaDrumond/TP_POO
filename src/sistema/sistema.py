import tkinter as tk
from tkinter import ttk
import json
import os
import hashlib
import datetime
import unicodedata
from usuario.cliente import Cliente
from usuario.administrador import Administrador

def normalizar_string(s: str) -> str: 
        return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')

class Sistema:
    def __init__(self, arquivo_dados: str="usuarios.json", arquivo_livros: str="livros.json") -> None:
        self.arquivo_dados = arquivo_dados
        self.arquivo_livros = arquivo_livros

        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'database'))
        
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
        self.arquivo_dados = os.path.join(self.base_dir, arquivo_dados)
        self.arquivo_livros = os.path.join(self.base_dir, arquivo_livros)
        
        self.carregar_dados()
        self.carregar_livros()
        
    def carregar_dados(self) -> None:
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as arquivo:
                self.usuarios = json.load(arquivo)
        except FileNotFoundError:
            self.usuarios = []

    def salvar_dados(self) -> None:
        with open(self.arquivo_dados, 'w', encoding='utf-8') as arquivo:
            json.dump(self.usuarios, arquivo, indent=4)

    def carregar_livros(self) -> None:
        try:
            with open(self.arquivo_livros, 'r', encoding='utf-8') as arquivo:
                self.livros = json.load(arquivo)
        except FileNotFoundError:
            self.livros = []

    def salvar_livros(self) -> None:
        with open(self.arquivo_livros, 'w', encoding='utf-8') as arquivo:
            json.dump(self.livros, arquivo, indent=4)

    def cadastrar_usuario(self, nome: str, email: str, senha: str, tipo: str) -> None:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        if not nome.isalpha():
            raise ValueError("O nome deve conter apenas letras.")

        if any(normalizar_string(usuario['nome']) == normalizar_string(nome) for usuario in self.usuarios):
            raise ValueError("O nome de usuário já existe.")

        if any(usuario['email'] == email for usuario in self.usuarios):
            raise ValueError("O email já está cadastrado.")

        self.usuarios.append({"nome": nome, "email": email, "senha": senha_hash, "tipo": tipo})
        self.salvar_dados()

    def autenticar_usuario(self, nome: str, senha: str) -> object:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        for usuario in self.usuarios:
            if normalizar_string(usuario['nome']) == normalizar_string(nome) and usuario['senha'] == senha_hash:
                if usuario['tipo'] == 'cliente':
                    cliente = Cliente(usuario['nome'], usuario['senha'])
                    cliente.livros_reservados = usuario.get("livros_reservados", [])
                    return cliente
                elif usuario['tipo'] == 'administrador':
                    return Administrador(usuario['nome'], usuario['senha'])
        raise ValueError("Nome ou senha incorretos.")
    
    def cadastrar_livro(self, titulo: str, autor: str, ano: int) -> None:
        titulo_normalizado = normalizar_string(titulo).lower()
        if any(normalizar_string(livro['titulo']).lower() == titulo_normalizado for livro in self.livros):
            raise ValueError("Já existe um livro com esse título.")

        self.livros.append({
        "titulo": titulo_normalizado,  
        "autor": autor,
        "ano": ano,
        "disponivel": True  
    })
        self.salvar_livros()


    def editar_livro(self, titulo_atual: str, novo_titulo: str, novo_autor: str, novo_ano: int) -> None:
        if not novo_titulo or not novo_autor or novo_ano <= 0:
            raise ValueError("Informações inválidas para o livro.")

        for livro in self.livros:
            if normalizar_string(livro['titulo']) == normalizar_string(titulo_atual):
                livro.update({"titulo": novo_titulo, "autor": novo_autor, "ano": novo_ano})
                self.salvar_livros()
                return
        raise ValueError("Livro não encontrado.")

    def remover_livro(self, titulo: str) -> dict:
        livro_removido = next((livro for livro in self.livros if normalizar_string(livro['titulo']) == normalizar_string(titulo)), None)
        if not livro_removido:
            raise ValueError("Livro não encontrado.")
        self.livros = [livro for livro in self.livros if normalizar_string(livro['titulo']) != normalizar_string(titulo)]
        self.salvar_livros()
        return livro_removido
    
    def reservar_livro(self, titulo_livro: str, cliente: Cliente, periodo: int) -> tuple:
        livro = next((l for l in self.livros if normalizar_string(l["titulo"]) == normalizar_string(titulo_livro)), None)
        if not livro:
            raise ValueError("Livro não encontrado.")
        if not livro.get("disponivel", True):
            raise ValueError("Livro indisponível para reserva.")

        valores_periodo = {5: 10.0, 10: 20.00}  # Definição do período de empréstimo e seu valor;
        valor = valores_periodo.get(periodo, None)
        if valor is None:
            raise ValueError("Período de empréstimo inválido.")
        
        data_reserva = datetime.date.today()
        data_devolucao = data_reserva + datetime.timedelta(days=periodo)

        for l in self.livros:
            if normalizar_string(l["titulo"]) == normalizar_string(titulo_livro):
                l["disponivel"] = False
                l["reserva"] = {
                    "cliente": cliente.nome,
                    "periodo": periodo,
                    "valor": valor,
                    "data_reserva": data_reserva.isoformat(),
                    "data_devolucao": data_devolucao.isoformat()
                }
                break

        cliente.adicionar_livro_reservado(livro)  # Adiciona o livro à lista de livros reservados do cliente

        try:
            self.salvar_livros()  # Salvando as alterações no arquivo
            self.salvar_dados()  # Salvando os dados do cliente
        except Exception as e:
            raise IOError(f"Erro ao salvar a reserva no arquivo: {str(e)}")

        return valor, data_reserva, data_devolucao
    
    def renovar_emprestimo(self, titulo_livro: str, cliente: Cliente, novo_periodo: int) -> float:
        #Renova o empréstimo de um livro reservado por um cliente.
        livro = next((l for l in self.livros if l["titulo"] == titulo_livro), None)
        if not livro:
            raise ValueError("Livro não encontrado.")

        if livro.get("reserva", {}).get("cliente") != cliente.nome:
            raise ValueError("Este livro não está reservado por você.")

        valores_periodo = {5: 10.0, 10: 20.0}  # Novo período e valores
        novo_valor = valores_periodo.get(novo_periodo, None)
        if novo_valor is None:
            raise ValueError("Período de empréstimo inválido.")

        # Atualizando a reserva
        livro["reserva"]["periodo"] = novo_periodo
        livro["reserva"]["valor"] = novo_valor

        # Salvando no arquivo
        try:
            self.salvar_livros()
        except Exception as e:
            raise IOError(f"Erro ao salvar a renovação no arquivo: {str(e)}")

        return novo_valor

    def devolver_livro(self, titulo_livro: str, cliente: Cliente) -> float:
        #Devolve um livro reservado e calcula a multa, se aplicável.
        livro = next((l for l in self.livros if l["titulo"] == titulo_livro), None)
        if not livro:
            raise ValueError("Livro não encontrado.")

        if livro.get("reserva", {}).get("cliente") != cliente.nome:
            raise ValueError("Este livro não está reservado por você.")

        # Verificar se há atraso e calcular multa
        reserva = livro.get("reserva", {})
        dias_reservados = reserva.get("periodo", 0)
        valor_reserva = reserva.get("valor", 0)
        dias_atraso = max(0, dias_reservados - 10)  # Simulação: prazo excedido após 10 dias

        multa = cliente.calcular_multa(livro, dias_atraso)

        # Tornar o livro disponível novamente
        livro["disponivel"] = True
        livro.pop("reserva", None)  # Remove a reserva do livro

        # Atualizar no arquivo
        try:
            self.salvar_livros()
        except Exception as e:
            raise IOError(f"Erro ao salvar a devolução no arquivo: {str(e)}")

        return multa