import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from cliente.tela_exibir_catalogo import TelaExibirCatalogo

class TelaRenovarDevolverLivro:
    def __init__(self, sistema: Sistema, cliente):
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Tk()
        self.root.title("Renovar ou Devolver Livro")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Renovar ou Devolver Livro", font=("Arial", 14, "bold")).pack(pady=20)

        self.livro_selecionado = tk.StringVar()
        
        # Exibir os livros reservados
        self.listar_livros_reservados()

        self.renovar_button = tk.Button(self.root, text="Renovar Empréstimo", command=self.renovar_emprestimo, width=30)
        self.renovar_button.pack(pady=5)

        self.devolver_button = tk.Button(self.root, text="Devolver Livro", command=self.devolver_livro, width=30)
        self.devolver_button.pack(pady=5)

        self.voltar_button = tk.Button(self.root, text="Voltar", command=self.voltar, width=30)
        self.voltar_button.pack(pady=5)

    def listar_livros_reservados(self):
        """Exibe os livros que o cliente tem reservado."""
        livros_reservados = [livro for livro in self.sistema.livros if "reserva" in livro and livro["reserva"]["cliente"] == self.cliente.nome]
        
        if not livros_reservados:
            messagebox.showinfo("Sem Reservas", "Você não tem livros reservados.")
            self.root.quit()
            return

        tk.Label(self.root, text="Escolha um livro para renovar ou devolver:", font=("Arial", 10)).pack(pady=10)
        
        for livro in livros_reservados:
            livro_button = tk.Radiobutton(self.root, text=livro["titulo"], value=livro["titulo"], variable=self.livro_selecionado)
            livro_button.pack(pady=2)

    def renovar_emprestimo(self):
        livro_titulo = self.livro_selecionado.get()
        if not livro_titulo:
            messagebox.showerror("Erro", "Selecione um livro para renovar.")
            return

        for livro in self.sistema.livros:
            if livro["titulo"] == livro_titulo and "reserva" in livro and livro["reserva"]["cliente"] == self.cliente.nome:
                livro["reserva"]["periodo"] += 5  # Renova por 5 dias, você pode ajustar isso
                messagebox.showinfo("Sucesso", f"O empréstimo do livro '{livro_titulo}' foi renovado por mais 5 dias.")
                return

        messagebox.showerror("Erro", "Não foi possível renovar o livro.")

    def devolver_livro(self):
        livro_titulo = self.livro_selecionado.get()
        if not livro_titulo:
            messagebox.showerror("Erro", "Selecione um livro para devolver.")
            return

        for livro in self.sistema.livros:
            if livro["titulo"] == livro_titulo and "reserva" in livro and livro["reserva"]["cliente"] == self.cliente.nome:
                livro["disponivel"] = True
                del livro["reserva"]
                messagebox.showinfo("Sucesso", f"O livro '{livro_titulo}' foi devolvido e está agora disponível.")
                return

        messagebox.showerror("Erro", "Não foi possível devolver o livro.")

    def voltar(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

