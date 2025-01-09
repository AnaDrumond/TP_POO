from interface.tela_login import TelaLogin
from sistema.sistema import Sistema

class Main:
    def __init__(self) -> None:
        self.sistema = Sistema()

    def iniciar(self) -> None:
        TelaLogin(self.sistema)

if __name__ == "__main__":
    app = Main()
    app.iniciar()