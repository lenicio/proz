def identificar_maiusculas(letra):
    if letra.isupper():
        return "Maiúscula"
    elif letra.islower():
        return "Minúscula"
    else:
        return "Entrada inválida!"


print(identificar_maiusculas(input("Insira uma letra: ")))
