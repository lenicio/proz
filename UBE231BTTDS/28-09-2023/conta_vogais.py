def contar_vogais(palavra):
    contador = 0

    for letra in palavra.lower():
        if letra in "aeiou":
            contador += 1

    return contador


print(contar_vogais("Banana"))
