import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente
from cliente.tela_exibir_catalogo import TelaExibirCatalogo
from cliente.tela_reservar_livro import TelaReservarLivro
from cliente.tela_devolver_livro import TelaDevolverLivro
from cliente.tela_renovar_emprestimo import TelaRenovarEmprestimo
from cliente.tela_ver_disponibilidade import TelaVerDisponibilidade

class TelaCliente:
    def __init__(self, sistema: Sistema, cliente: Cliente) -> None:
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Tk()
        self.root.title("Painel do Cliente")
        self.root.geometry("800x600")

        self.root.configure(bg="#013440")
    
        tk.Label(self.root, text="Bem-vindo ao Painel do Cliente!", font=("Arial", 14, "bold"), bg="#013440", fg="white").pack(pady=20)

        tk.Button(self.root, text="Ver Catálogo de Livros", command=self.ver_catalogo, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Reservar Livro", command=self.reservar_livro, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Devolver Livro", command=self.devolver_livro, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Renovar Empréstimo", command=self.renovar_emprestimo, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Ver Disponibilidade do Livro", command=self.ver_disponibilidade, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Ver Multas", command=self.ver_multas, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Pagar Multas", command=self.pagar_multas, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)
        tk.Button(self.root, text="Fale Conosco", command=self.fale_conosco, bg="#4A5D23", fg="white", font=("Arial", 12, "bold"), width=30).pack(pady=5)

    def ver_catalogo(self) -> None:
        TelaExibirCatalogo(self.sistema)

    def reservar_livro(self) -> None:
        TelaReservarLivro(self.sistema, self.cliente)

    def devolver_livro(self) -> None:
        TelaDevolverLivro(self.sistema, self.cliente)    

    def renovar_emprestimo(self) -> None:
        TelaRenovarEmprestimo(self.sistema, self.cliente)

    def ver_disponibilidade(self) -> None:
        TelaVerDisponibilidade(self.sistema, self.cliente)
    
    def ver_multas(self) -> None:
        multa_total = self.cliente.get_multa_total()
        if multa_total > 0:
            messagebox.showinfo("Multas", f"Total de multas acumuladas: R$ {multa_total:.2f}")
        else:
            messagebox.showinfo("Multas", "Você não possui multas pendentes.")

    def pagar_multas(self) -> None:
        multa_total = self.cliente.get_multa_total()
        if multa_total > 0:
            self.cliente.multa_total = 0 
            messagebox.showinfo("Pagamento", "Todas as multas foram pagas com sucesso!")
        else:
            messagebox.showinfo("Pagamento", "Você não possui multas para pagar.")   

    def fale_conosco(self) -> None:
        messagebox.showinfo("Fale Conosco", "Contato: biblioteca@exemplo.com\nTelefone: (31) 1234-5678")
