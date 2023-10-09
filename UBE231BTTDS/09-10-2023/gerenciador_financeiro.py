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
    print("[3] - Exibir Totais")
    print("[4] - Sair")
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

    elif opcao == "2":
        print(transacoes)

    elif opcao == "3":
        receitas = []
        despesas = []
        for item in transacoes:
            if item['valor'] > 0:
                receitas.append(item['valor'])
            else:
                despesas.append(item['valor'])

        print(f"Receitas: {sum(receitas):.2f}")
        print(f"Despesas: {sum(despesas):.2f}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção Inválida!")
        input("\n\nPressione qualquer tecla para continuar...")
