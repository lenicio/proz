import arquivo
from os import system

if __name__ == "__main__":
    todo = []
    while True:
        system("cls")
        print("[1] - Adicionar tarefa")
        print("[2] - Listar tarefas")
        print("[3] - Sair")
        comando = input("Selecione: ")

        if comando == "1":
            todo.append(input("Insira a atividade: "))
            arquivo.criar_arquivo("todo.json", todo)

        elif comando == "2":
            dados = arquivo.ler_arquivo("todo.json")

            for item in dados:
                print(f"{item}")

            input("\n\nPressione qualquer tecla para continuar...")

        elif comando == "3":
            break

        else:
            print("Opção inválida!")
            input("\n\nPressione qualquer tecla para continuar...")
