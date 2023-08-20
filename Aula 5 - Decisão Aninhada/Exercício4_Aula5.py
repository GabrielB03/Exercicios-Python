 #Exercício 4

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Especifique a operação pretendida ( + | - | * | /): ")

if op== "+":
    soma = n1 + n2
    print("O valor da soma é: ", soma)

elif op== "-":
    sub = n1 - n2
    print("O valor da subtração é: ", sub)

elif op== "*":
    mult = n1 * n2
    print("O valor da multiplicação é: ", mult)

elif op== "/":
    div = n1 / n2
    print("O valor da divisão é: ", div)

else:
    print("Operação inválida")