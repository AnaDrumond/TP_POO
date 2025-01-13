import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente
import unicodedata

def normalizar_string(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')

class TelaVerDisponibilidade:
    def __init__(self, sistema: Sistema, cliente: Cliente) -> None:
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Tk()
        self.root.title("Ver Disponibilidade do Livro")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Digite o título do livro para verificar a disponibilidade:").pack(pady=10)
        self.titulo_entry = tk.Entry(self.root, width=40)
        self.titulo_entry.pack(pady=10)

        tk.Button(self.root, text="Verificar Disponibilidade", command=self.verificar_disponibilidade).pack(pady=5)

    def verificar_disponibilidade(self) -> None:
        titulo = self.titulo_entry.get()
        titulo_normalizado = normalizar_string(titulo).lower()
    
        livro_encontrado = next(
            (livro for livro in self.sistema.livros if normalizar_string(livro["titulo"]).lower() == titulo_normalizado),
            None
        )

        if livro_encontrado:
            if livro_encontrado.get("disponivel", True):
                messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está disponível para empréstimo.")
            else:
                if "reserva" in livro_encontrado:
                    messagebox.showinfo(
                        "Disponibilidade", 
                        f"O livro '{titulo}' está reservado para {livro_encontrado['reserva']['cliente']} por {livro_encontrado['reserva']['periodo']} dias."
                    )
                else:
                    messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está indisponível no momento.")
        else:
            messagebox.showerror("Erro", "Livro não encontrado no catálogo.")