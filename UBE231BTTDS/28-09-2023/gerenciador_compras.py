from os import system


def main():
    lista_de_compras = []

    print("Bem-vindo à sua lista de compras!\n")

    while True:
        system("cls")
        print("Sua lista atual:")
        print(lista_de_compras)

        item = input("\nDigite um item para adicionar à lista ou 'sair' para terminar: ").strip()

        if item.lower() == "sair":
            break
        elif item:
            lista_de_compras.append(item)

    print("\nObrigado por usar o programa!")


if __name__ == "__main__":
    main()
