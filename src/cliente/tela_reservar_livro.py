import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from sistema.sistema import Sistema
from usuario.cliente import Cliente

class TelaReservarLivro:
    def __init__(self, sistema: Sistema, cliente: Cliente) -> None:
        self.sistema = sistema
        self.cliente = cliente

        self.root = tk.Toplevel()
        self.root.title("Reservar Livro")

        tk.Label(self.root, text="Catálogo de Livros Disponíveis").pack(pady=10)

        # Tabela de livros
        self.treeview = ttk.Treeview(self.root, columns=("Título", "Autor", "Ano", "Disponível"), show="headings", height=10)
        self.treeview.heading("Título", text="Título")
        self.treeview.heading("Autor", text="Autor")
        self.treeview.heading("Ano", text="Ano")
        self.treeview.heading("Disponível", text="Disponível")
        
        self.treeview.column("Título", width=300)
        self.treeview.column("Autor", width=200)
        self.treeview.column("Ano", width=50)
        self.treeview.column("Disponível", width=100)

        self.treeview.pack(pady=10)

        self.carregar_livros_na_tabela()

        tk.Button(self.root, text="Reservar", command=self.reservar).pack(pady=10)

    def carregar_livros_na_tabela(self) -> None:
        livros_disponiveis = self.get_livros_disponiveis()
        for livro in livros_disponiveis:
            disponivel = "Sim" if livro.get("disponivel", True) else "Não"
            self.treeview.insert("", "end", values=(livro["titulo"], livro["autor"], livro["ano"], disponivel))

    def get_livros_disponiveis(self) -> list:
        return [livro for livro in self.sistema.livros if livro.get("disponivel", True)]

    def reservar(self)-> None:
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um livro para reservar.")
            return
        
        item_values = self.treeview.item(selected_item, "values")
        titulo_livro = item_values[0] 

        try:
            periodo = simpledialog.askinteger("Período de Empréstimo", "Escolha o período (5 ou 10 dias):")
            if periodo not in [5, 10]:
                raise ValueError("Período de empréstimo inválido. Escolha 5 ou 10 dias.")
            
            valor, data_reserva, data_devolucao = self.sistema.reservar_livro(titulo_livro, self.cliente, periodo)
            messagebox.showinfo("Reserva Confirmada", f"Livro reservado com sucesso!\nValor: R${valor:.2f}\nData de Reserva: {data_reserva}\nData de Devolução: {data_devolucao}")
            
            self.treeview.delete(*self.treeview.get_children())
            self.carregar_livros_na_tabela()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", "Ocorreu um erro ao tentar reservar o livro.") #Mensagem de erro para o cliente
            #messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}") Mensagem de erro para a programadora    
     
