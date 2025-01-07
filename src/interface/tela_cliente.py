import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente
from cliente.tela_exibir_catalogo import TelaExibirCatalogo
from cliente.tela_reservar_livro import TelaReservarLivro
from cliente.tela_renovar_devolver_livro import TelaRenovarDevolverLivro
from cliente.tela_ver_disponibilidade import TelaVerDisponibilidade

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
        tk.Button(self.root, text="Ver Disponibilidade do Livro", command=self.ver_disponibilidade, width=30).pack(pady=5)
        tk.Button(self.root, text="Ver Multas", command=self.ver_multas, width=30).pack(pady=5)
        tk.Button(self.root, text="Pagar Multas", command=self.pagar_multas, width=30).pack(pady=5)
        tk.Button(self.root, text="Fale Conosco", command=self.fale_conosco, width=30).pack(pady=5)

    def ver_catalogo(self):
        TelaExibirCatalogo(self.sistema)

    def reservar_livro(self):
        TelaReservarLivro(self.sistema, self.cliente)

    def devolver_livro(self):
        titulo_livro = tk.simpledialog.askstring("Devolver Livro", "Informe o título do livro:")
        if not titulo_livro:
            return

        try:
            multa = self.sistema.devolver_livro(titulo_livro, self.cliente)
            if multa > 0:
                messagebox.showinfo("Livro Devolvido", f"Livro devolvido com sucesso!\nMulta: R$ {multa:.2f}")
            else:
                messagebox.showinfo("Livro Devolvido", "Livro devolvido com sucesso!\nNenhuma multa aplicada.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")
            
    # Depois vou tentar arrumar essas duas funções num outro arquivo igual as outras pra deixar tudo bonitnho

    def renovar_emprestimo(self):
        titulo_livro = tk.simpledialog.askstring("Renovar Empréstimo", "Informe o título do livro:")
        if not titulo_livro:
            return

        novo_periodo = tk.simpledialog.askinteger("Renovar Empréstimo", "Informe o novo período (5 ou 10 dias):")
        if not novo_periodo:
            return

        try:
            valor = self.sistema.renovar_emprestimo(titulo_livro, self.cliente, novo_periodo)
            messagebox.showinfo("Renovação Concluída", f"Empréstimo renovado com sucesso!\nNovo valor: R$ {valor:.2f}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")

    def ver_disponibilidade(self):
        TelaVerDisponibilidade(self.sistema, self.cliente)
    
    def ver_multas(self):
        multa_total = self.cliente.get_multa_total()
        if multa_total > 0:
            messagebox.showinfo("Multas", f"Total de multas acumuladas: R$ {multa_total:.2f}")
        else:
            messagebox.showinfo("Multas", "Você não possui multas pendentes.")

    def pagar_multas(self):
        multa_total = self.cliente.get_multa_total()
        if multa_total > 0:
            self.cliente.multa_total = 0  # Zera as multas do cliente
            messagebox.showinfo("Pagamento", "Todas as multas foram pagas com sucesso!")
        else:
            messagebox.showinfo("Pagamento", "Você não possui multas para pagar.")   

    def fale_conosco(self):
        messagebox.showinfo("Fale Conosco", "Contato: biblioteca@exemplo.com\nTelefone: (31) 1234-5678")
