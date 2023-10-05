lista = list(map(int, input("Insira suas notas separadas por vírgula: ").split(", ")))

media = sum(lista) / len(lista)

print(f"Média: {media:.1f}")
