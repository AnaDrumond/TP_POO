from interface.tela_login import TelaLogin
from sistema.sistema import Sistema

if __name__ == "__main__":
    sistema = Sistema()
    TelaLogin(sistema)