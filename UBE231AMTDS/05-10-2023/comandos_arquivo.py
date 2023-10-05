# write  - Criar ou Sobrescrever um arquivo
# read   - Lê o conteúdo de um arquivo
# append - Adiciona informações a um arquivo existente
# +      - Adiciona capacidade de leitura/escrita

# Cria um arquivo e adiciona informações nele
with open("nome.txt", "w") as arquivo:
    arquivo.write("Nome: ")
    arquivo.write(input("Insira seu nome: ") + "\n")

# Adiciona informações ao arquivo aberto anteriormente
with open("nome.txt", "a") as arquivo:
    arquivo.write("Idade: ")
    arquivo.write(input("Informe sua idade: ") + "\n")

# Realiza a leitura do conteúdo do arquivo e direciona para uma variável
with open("nome.txt", "r") as arquivo:
    ret = arquivo.read()

print(ret)


