from os import system

lista_cadastro = [
    {'titulo': 'Orgulho e Preconceito', 'genero': 'Romance', 'isbn': '123451'},
    {'titulo': '1984', 'genero': 'Ficção Distópica', 'isbn': '123452'},
    {'titulo': 'O Senhor dos Anéis', 'genero': 'Fantasia', 'isbn': '123453'},
    {'titulo': 'Cem Anos de Solidão', 'genero': 'Romance', 'isbn': '123454'},
    {'titulo': 'Moby Dick', 'genero': 'Aventura', 'isbn': '123455'},
    {'titulo': 'O Grande Gatsby', 'genero': 'Romance', 'isbn': '123456'},
    {'titulo': 'O Apanhador no Campo de Centeio', 'genero': 'Romance', 'isbn': '123457'},
    {'titulo': 'Fahrenheit 451', 'genero': 'Ficção Distópica', 'isbn': '123458'},
    {'titulo': 'Dom Quixote', 'genero': 'Aventura', 'isbn': '123459'},
    {'titulo': 'A Revolução dos Bichos', 'genero': 'Fábula', 'isbn': '1234510'}
]

while True:
    system("cls")
    print("[1] - Cadastrar novo livro")
    print("[2] - Listar Livros")
    print("[3] - Buscar Livro")
    print("[4] - Encerrar")
    opcao = input("Selecione: ")

    if opcao == "1":
        cadastro = {
            "titulo": input("Informe o título do livro: "),
            "isbn": input("Informe o isbn do livro: "),
            "genero": input("Informe o genero do livro: ")
        }

        lista_cadastro.append(cadastro)
        print("\n\nLivro cadastrado com sucesso!")

    elif opcao == "2":
        for item in lista_cadastro:
            print(f"Título: {item['titulo']}")
            print(f"isbn: {item['isbn']}")
            print(f"Genero: {item['genero']}")
            print("-" * 70)

    elif opcao == "3":
        isbn = input("Informe o ISBN a ser pesquisado: ")

        encontrou_livro = False
        for item in lista_cadastro:
            if isbn == item['isbn']:
                print(f"Título: {item['titulo']}")
                print(f"isbn: {item['isbn']}")
                print(f"Genero: {item['genero']}")
                encontrou_livro = True

        if not encontrou_livro:
            print("Livro não encontrado!")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")

    input("\n\nPressione qualquer tecla para continuar...")
