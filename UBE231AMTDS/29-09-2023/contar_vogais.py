def contar_vogais(palavra):

    contador = 0
    for letra in palavra:
        if letra.lower() in "aeiou":
            contador += 1

    return contador


print(contar_vogais("Casa Grande"))
