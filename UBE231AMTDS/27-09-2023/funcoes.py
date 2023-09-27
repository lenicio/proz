from os import system


def limpa_tela():
    system("cls")


def imprime_menu():
    print("[1] - Adicionar")
    print("[2] - Listar")
    print("[3] - Editar")
    print("[4] - Remover")


def adiciona_celular(lista):
    novo_celular = {
        "modelo": input("Informe o modelo: "),
        "fabricante": input("Informe o fabricante: ")
    }

    lista.append(novo_celular)
    print("\nModelo adicionado com sucesso!")

    input("\n\nPressione qualquer tecla para continuar...")


def listar_celulares(lista):
    for item in lista:
        print(f"Modelo: {item['modelo']} - {item['fabricante']}")

    input("\n\nPressione qualquer tecla para continuar...")


if __name__ == "__main__":

    lista_celulares = [
        {"modelo": "Iphone 15", "fabricante": "Apple"},
        {"modelo": "Samsung Galaxy S30", "fabricante": "Samsung"},
        {"modelo": "Google Pixel 8", "fabricante": "Google"},
        {"modelo": "OnePlus 10", "fabricante": "OnePlus"},
        {"modelo": "LG G9", "fabricante": "LG"},
        {"modelo": "Motorola Moto G100", "fabricante": "Motorola"},
        {"modelo": "Huawei P60", "fabricante": "Huawei"},
        {"modelo": "Xiaomi Mi 13", "fabricante": "Xiaomi"},
        {"modelo": "Sony Xperia Z6", "fabricante": "Sony"},
        {"modelo": "Nokia 11", "fabricante": "Nokia"}
    ]

    while True:
        limpa_tela()
        imprime_menu()
        opcao = input("Selecione: ")

        if opcao == "1":
            adiciona_celular(lista_celulares)

        if opcao == "2":
            listar_celulares(lista_celulares)


