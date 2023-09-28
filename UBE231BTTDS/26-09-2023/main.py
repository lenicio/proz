from os import system
from random import choice

mostrar_forca = ["""
     --------
    /       |
    |       
    |
    |
    |
    |
-----------""",               
"""
     --------
    /       |
    |       O 
    |
    |
    |
    |
-----------""",
"""
     --------
    /       |
    |       O 
    |       |
    |
    |
    |
-----------""",
"""
     --------
    /       |
    |       O 
    |      /|
    |
    |
    |
-----------""",
"""
     --------
    /       |
    |       O 
    |      /|\\
    |
    |
    |
-----------""",
"""
     --------
    /       |
    |       O 
    |      /|\\
    |      /
    |
    |
-----------""",
"""
     --------
    /       |
    |       O 
    |      /|\\
    |      / \\
    |
    |
-----------"""
]

if __name__ == "__main__":
    palavra_secreta = "banana"
    letras_erradas = []
    jogo = ['_' for letra in palavra_secreta]
    
    erros = 0
    while True:
        system("clear")
        print(mostrar_forca[erros], end=f'{" ":<12}')
        print(*jogo, sep=' ')
        print('-'*50)
        chute = input("Informe a letra: ")

        # Verifica se a letra que o usuario chutou existe na palavra secreta
        if chute in palavra_secreta:
            indice = 0

            # Itera sobre a palavra secreta, onde cada loop representa uma letra
            for letra in palavra_secreta:
                if letra == chute:
                    jogo[indice] = letra  # Edita a lista jogo, substituindo o _ pela letra correta
                indice += 1
        else:
            erros += 1  # Caso a letra não exista dentro da palavra, ele adicionará +1 a variavel erros
            letras_erradas.append(chute)  # Adiciona a letra errada dentro de uma lista

        if erros == 6:
            system('clear')
            print(mostrar_forca[erros])
            print('='*50)
            print("Você foi enforcado!")
            print(f'A palavra era {palavra_secreta}')
            print('='*50)
            break

        if "_" not in jogo:
            system('clear')
            print('='*50)
            print("Parabéns, você acertou!")
            print('='*50)
            break
