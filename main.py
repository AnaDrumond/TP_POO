from models.user_model import UserModel
from views.login_view import LoginView
import tkinter as tk

if __name__ == "__main__":
    # Inicialize o arquivo de usuários
    UserModel.inicializar_arquivo()

    # Inicie a interface
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
