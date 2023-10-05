nf = float(input("Insira a nota final: "))

if nf < 0 or nf > 10:
    print("Nota inválida!")

elif nf >= 6:
    print("Aprovado!")

elif nf >= 4:
    print("Recuperação!")

else:
    print("Reprovado!")
