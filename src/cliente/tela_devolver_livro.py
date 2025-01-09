import tkinter as tk
from tkinter import messagebox
from sistema.sistema import Sistema
from usuario.cliente import Cliente

class TelaDevolverLivro:
    def __init__(self, sistema: Sistema, cliente: Cliente) -> None:
        self.sistema = sistema
        self.cliente = cliente
        self.root = tk.Toplevel()
        self.root.title("Devolver Livro")
        self.root.geometry("400x200")

        tk.Label(self.root, text="Devolver Livro", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Label(self.root, text="Título do Livro:").pack(pady=5)
        self.titulo_entry = tk.Entry(self.root, width=30)
        self.titulo_entry.pack(pady=5)

        tk.Button(self.root, text="Devolver", command=self.devolver_livro, width=30).pack(pady=20)

    def devolver_livro(self) -> None:
        titulo_livro = self.titulo_entry.get()
        if not titulo_livro:
            return

        try:
            multa = self.sistema.devolver_livro(titulo_livro, self.cliente)
            if multa > 0:
                messagebox.showinfo("Livro Devolvido", f"Livro devolvido com sucesso!\nMulta: R$ {multa:.2f}")
            else:
                messagebox.showinfo("Livro Devolvido", "Livro devolvido com sucesso!\nNenhuma multa aplicada.")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")