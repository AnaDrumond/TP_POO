import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente

class TelaVerDisponibilidade:
    def __init__(self, sistema: Sistema, cliente: Cliente):
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Tk()
        self.root.title("Ver Disponibilidade do Livro")
        self.root.geometry("400x300")

        # Criar campo para o cliente digitar o título do livro
        tk.Label(self.root, text="Digite o título do livro para verificar a disponibilidade:").pack(pady=10)
        self.titulo_entry = tk.Entry(self.root, width=40)
        self.titulo_entry.pack(pady=10)

        # Botão para verificar a disponibilidade
        tk.Button(self.root, text="Verificar Disponibilidade", command=self.verificar_disponibilidade).pack(pady=5)

    def verificar_disponibilidade(self):
        # Obter o título do livro
        titulo = self.titulo_entry.get()
        
        # Procurar o livro no sistema
        livro_encontrado = None
        for livro in self.sistema.livros:  # Supondo que 'livros' é a lista de livros do sistema
            if livro["titulo"].lower() == titulo.lower():
                livro_encontrado = livro
                break
        
        if livro_encontrado:
            # Mostrar a disponibilidade
            if livro_encontrado["disponivel"]:
                messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está disponível para empréstimo.")
            else:
                # Verificar se o livro tem reserva
                if "reserva" in livro_encontrado:
                    messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está reservado para {livro_encontrado['reserva']['cliente']} por {livro_encontrado['reserva']['periodo']} dias.")
                else:
                    messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está indisponível no momento.")
        else:
            messagebox.showerror("Erro", "Livro não encontrado no catálogo.")
