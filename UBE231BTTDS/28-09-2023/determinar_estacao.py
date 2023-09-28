def determinar_estacao(mes):
    estacao = ""
    if mes in [3, 4, 5]:
        estacao = "Primavera"

    elif mes in [6, 7, 8]:
        estacao = "Verão"

    elif mes in [9, 10, 11]:
        estacao = "Outono"

    elif mes in [12, 1, 2]:
        estacao = "Inverno"

    else:
        return "O mês precisa ser entre 1 e 12."

    return estacao


print(determinar_estacao(1))
