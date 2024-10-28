from tkinter import*
import tkinter #importando componentes

# --- TRECHO QUE CRIA UMA TELA COM UM WIDGET ---

#class Application:
 #   def __init__(self, master=None):
  #      self.widget1 = Frame(master) #cria o container 'widget1', e passa como referência o container mestre
   #     #o frame 'master' é o elemento máximo da hierarquia, a janela de aplicação
    #    self.widget1.pack() #foi escolhido o gerenciador de geometria 'pack'
     #   self.mensagem = Label(self.widget1, text="Primeiro Widget")
      #  self.mensagem.pack()
    
#root = Tk()
#Application(root)
#root.mainloop() #exibe na tela

# --- TRECHO QUE CRIA WIDGETS MAIS CUSTOMIZÁVEIS --- 

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.mensagem = Label(self.widget1, text="Primeiro widget")
        self.mensagem["font"] = ("Calibri", "10", "italic") #definições estéticas do texto
        self.mensagem.pack ()
        self.sair = Button(self.widget1) #o widget está sempre associado ao clique do mouse
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack ()

    def mudarTexto(self): #método event handler 
        if self.mensagem["text"] == "Primeiro widget":
            self.mensagem["text"] = "O botão recebeu um clique"
        else:
            self.mensagem["text"] = "Primeiro widget"



root = Tk()
Application(root)
root.mainloop()