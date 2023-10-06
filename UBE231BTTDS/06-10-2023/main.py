import funcoes_arquivo

while True:
    cad = input("Adicione um item a lista de compras, "
                "ou digite sair: ")

    if cad.lower() == "sair":
        break

    funcoes_arquivo.adiciona_arquivo(cad, "lista_compras.txt")
