import json
import os

NOME_ARQUIVO = "transacoes.json"

if os.path.exists(NOME_ARQUIVO):
    with open("transacoes.json", "r") as matheus:
        transacoes = json.load(matheus)
else:
    transacoes = []


while True:
    print("[1] - Adicionar Transação")
    print("[2] - Listar Transações")
    print("[3] - Sair")
    opcao = input("Selecione: ")

    if opcao == "1":
        transacao = {
            "data_mvto": input("Informe a data: "),
            "valor": float(input("Informe o valor (-) para despesas: ")),
            "descricao": input("Informe a descrição: "),
            "categoria": input("Informe a categoria. Ex (Alimentação, Transporte, Etc...): ")
        }
        transacoes.append(transacao)
        with open(NOME_ARQUIVO, "w") as a:
            json.dump(transacoes, a)

    if opcao == "2":
        print(transacoes)
