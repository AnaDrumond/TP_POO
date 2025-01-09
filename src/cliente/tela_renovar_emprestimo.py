import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente

class TelaRenovarEmprestimo:
    def __init__(self, sistema: Sistema, cliente: Cliente) -> None:
        self.sistema = sistema
        self.cliente = cliente
        self.root = tk.Toplevel()
        self.root.title("Renovar Empréstimo")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Renovar Empréstimo", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Label(self.root, text="Título do Livro:").pack(pady=5)
        self.titulo_livro_entry = tk.Entry(self.root, width=30)
        self.titulo_livro_entry.pack(pady=5)

        tk.Label(self.root, text="Novo Período (5 ou 10 dias):").pack(pady=5)
        self.novo_periodo_entry = tk.Entry(self.root, width=30)
        self.novo_periodo_entry.pack(pady=5)

        tk.Button(self.root, text="Renovar", command=self.renovar_emprestimo, width=30).pack(pady=20)

    def renovar_emprestimo(self) -> None:
        titulo_livro = self.titulo_livro_entry.get()
        if not titulo_livro:
            return

        try:
            novo_periodo = int(self.novo_periodo_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Período inválido. Informe um número.")
            return

        try:
            valor = self.sistema.renovar_emprestimo(titulo_livro, self.cliente, novo_periodo)
            messagebox.showinfo("Renovação Concluída", f"Empréstimo renovado com sucesso!\nNovo valor: R$ {valor:.2f}")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")