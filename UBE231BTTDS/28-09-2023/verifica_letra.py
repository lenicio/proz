def identificar_maiuscula(letra):
    if letra.islower():
        return "Minúsculo"

    elif letra.isupper():
        return "Maiúsculo"

    else:
        return "Você precisa informar uma letra!"


print(identificar_maiuscula("A"))
