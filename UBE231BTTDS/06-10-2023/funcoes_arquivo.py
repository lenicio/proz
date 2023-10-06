# w     write   -> Permite criar ou sobrescrever um arquivo
# r     read    -> Permite ler o conteúdo de um arquivo
# a     append  -> Permite criar ou adicionar conteúdo a um arquivo

# write         -> Grava conteúdo dentro do arquivo


def adiciona_arquivo(conteudo, nome_arquivo):
    with open(nome_arquivo, "a") as a:
        a.write(conteudo + "\n")


def limpa_arquivo(nome_arquivo):
    with open(nome_arquivo, "w") as a:
        a.write("")
