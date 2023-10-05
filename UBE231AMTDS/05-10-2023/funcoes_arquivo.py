def limpar_arquivo(nome_arquivo):
    with open(nome_arquivo, "w") as a:
        a.write("")


def adicionar_arquivo(itens, nome_arquivo):
    with open(nome_arquivo, "a") as a:
        a.write(itens + "\n")

