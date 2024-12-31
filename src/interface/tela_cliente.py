import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente
from cliente.tela_exibir_catalogo import TelaExibirCatalogo
from cliente.tela_reservar_livro import TelaReservarLivro
from cliente.tela_renovar_devolver_livro import TelaRenovarDevolverLivro

class TelaCliente:
    def __init__(self, sistema: Sistema, cliente: Cliente):
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Tk()
        self.root.title("Painel do Cliente")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Bem-vindo ao Painel do Cliente!", font=("Arial", 14, "bold"), wraplength=180).pack(pady=20)

        tk.Button(self.root, text="Ver Catálogo de Livros", command=self.ver_catalogo, width=30).pack(pady=5)
        tk.Button(self.root, text="Reservar Livro", command=self.reservar_livro, width=30).pack(pady=5)
        tk.Button(self.root, text="Devolver Livro", command=self.devolver_livro, width=30).pack(pady=5)
        tk.Button(self.root, text="Renovar Empréstimo", command=self.renovar_emprestimo, width=30).pack(pady=5)
        tk.Button(self.root, text="Ver Multas", command=self.ver_multas, width=30).pack(pady=5)
        tk.Button(self.root, text="Fale Conosco", command=self.fale_conosco, width=30).pack(pady=5)

    def ver_catalogo(self):
        TelaExibirCatalogo(self.sistema)

    def reservar_livro(self):
        TelaReservarLivro(self.sistema, self.cliente)

    def devolver_livro(self):
        TelaRenovarDevolverLivro(self.sistema, self.cliente, action="devolver")

    def renovar_emprestimo(self):
        TelaRenovarDevolverLivro(self.sistema, self.cliente, action="renovar")

    def ver_multas(self):
        messagebox.showinfo("Multas", "Função em construção.")

    def fale_conosco(self):
        messagebox.showinfo("Fale Conosco", "Contato: biblioteca@exemplo.com\nTelefone: (31) 1234-5678")
