from contextlib import ContextDecorator


n = int(input("Digite um número inteiro e positivo: "))
contador = 0
soma = 0

while contador <= n:
    contador+=1
    soma += (1/contador)
    if contador == n:
        print(soma)