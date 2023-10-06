import json

with open("cadastro.json", "r") as a:
    lista_cadastro = json.load(a)

print(type(lista_cadastro))
