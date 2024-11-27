import json
import os


filename = "biblioteca.json"


if not os.path.exists(filename):
   
    data = {
        "livros": [],
        "usuarios": [],
        "emprestimos": []
    }

    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Arquivo {filename} criado com sucesso!")
else:
    print(f"O arquivo {filename} já existe.")
