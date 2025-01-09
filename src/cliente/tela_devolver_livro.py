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

        tk.Label(self.root, text="Selecione o Livro:").pack(pady=5)
        self.livro_var = tk.StringVar(value="")
        livros_opcoes = [f"{livro['titulo']} - {livro['autor']} ({livro['ano']})" for livro in self.sistema.livros if livro.get("reserva", {}).get("cliente") == cliente.nome]
        self.livro_menu = tk.OptionMenu(self.root, self.livro_var, *livros_opcoes)
        self.livro_menu.pack(pady=5)

        tk.Button(self.root, text="Devolver", command=self.devolver_livro, width=30).pack(pady=20)

    def devolver_livro(self) -> None:
        livro_selecionado = self.livro_var.get()
        if not livro_selecionado:
            messagebox.showerror("Erro", "Nenhum livro selecionado.")
            return

        titulo_livro = livro_selecionado.split(" - ")[0]  # Extrai o título original

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