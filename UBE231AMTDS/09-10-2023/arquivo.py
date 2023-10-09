import json


def criar_arquivo(nome_arquivo, valores):
    with open(nome_arquivo, "w") as a:
        json.dump(valores, a)