n = int(input("Insira um número inteiro: "))

fatorial = 1
while n > 0:
    fatorial = fatorial * n
    n -= 1

print(fatorial)
