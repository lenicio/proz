lista = ["Lucas", "Maria", "Pedro", "Julia"]

nome = input("Informe o nome a ser pesquisado: ")
if nome in lista:
    print(f"O nome {nome} está na lista!")
else:
    print(f"O nome {nome} não está na lista!")
