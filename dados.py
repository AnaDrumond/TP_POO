import json
import os

# Definir o caminho do arquivo JSON
filename = "biblioteca.json"

# Verificar se o arquivo já existe
if not os.path.exists(filename):
    # Estrutura inicial do arquivo JSON
    data = {
        "livros": [],
        "usuarios": [],
        "emprestimos": []
    }

    # Salvar a estrutura inicial no arquivo JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Arquivo {filename} criado com sucesso!")
else:
    print(f"O arquivo {filename} já existe.")
