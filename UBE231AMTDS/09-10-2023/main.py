import arquivo

if __name__ == "__main__":
    todo = []
    while True:
        comando = input("Digite uma tarefa, ou escreva sair: ")
        if comando.lower() == "sair":
            arquivo.criar_arquivo("todo.json", todo)
            break

        todo.append(comando)
