from interface.tela_login import TelaLogin
from sistema.sistema import Sistema

def main() -> None:
    sistema = Sistema()
    TelaLogin(sistema)

if __name__ == "__main__":
    main()