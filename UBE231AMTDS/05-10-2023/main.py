import funcoes_arquivo

for _ in range(5):
    nome = input("Informe o nome da fruta: ")
    funcoes_arquivo.adicionar_arquivo(nome, "frutas.txt")