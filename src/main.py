from interface.tela_login import TelaLogin
from sistema.sistema import Sistema
from usuario.cliente import Cliente

if __name__ == "__main__":
    sistema = Sistema()
    cliente = Cliente("self._nome", "senha_cliente") 
    #No 'livros.json' o nome do cliente que fez a reserva não está sendo passado como um dado coletado...Tenho
    #que ver como arrumar isso.
    TelaLogin(sistema,cliente)
    
      