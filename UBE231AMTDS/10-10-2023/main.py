import json
import os


NOME_ARQUIVO = "transacoes.json"
if os.path.exists(NOME_ARQUIVO):
    with open(NOME_ARQUIVO, "r") as a:
        transacoes = json.load(a)
else:
    transacoes = []

while True:
    os.system("cls")
    print("Menu".center(50, "."))
    print(". [1] - Adicionar ".ljust(50, "."))
    print(". [2] - Listar ".ljust(50, "."))
    print(". [3] - Exibir totais ".ljust(50, "."))
    print(". [4] - Encerrar ".ljust(50, "."))
    opcao = input(". Selecione: ")
    print("." * 50)

    if opcao == "1":
        transacao = {
            "data": input("Informe a data: "),
            "valor": float(input("Informe o valor, (-) para despesas: ")),
            "descricao": input("Informe a descrição: "),
            "categoria": input("Informe a categoria: ")
        }

        transacoes.append(transacao)

        with open("transacoes.json", "w") as a:
            json.dump(transacoes, a)

        input("\n\nPressione qualquer tecla para continuar...")
    elif opcao == "2":
        for item in transacoes:
            print(f"{item['data']}\n{item['descricao']}\nR${item['valor']:.2f}\n{item['categoria']}")
            print("-" * 50)

        input("\n\nPressione qualquer tecla para continuar...")

    elif opcao == "3":
        receitas = []
        despesas = []
        for item in transacoes:
            if item["valor"] >= 0:
                receitas.append(item["valor"])
            else:
                despesas.append(item["valor"])

        print(f"Despesas: {sum(despesas)}")
        print(f"Receitas: {sum(receitas)}")

        input("\n\nPressione qualquer tecla para continuar...")


