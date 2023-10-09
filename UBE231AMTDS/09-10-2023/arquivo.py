import json


def criar_arquivo(nome_arquivo, valores):
    with open(nome_arquivo, "w") as a:
        json.dump(valores, a)


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as a:
        return json.load(a)
