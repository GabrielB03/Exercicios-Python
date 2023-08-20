#exercício 1
lado1 = float(input("Digite o valor do maior lado do retângulo: "))
lado2 = float(input("Digite o valor do menor lado do retângulo: "))
perimetro = lado1 + lado2
area = lado1 * lado2

print("O perimetro desse retângulo é igual a: ", perimetro)
print("A área desse retângulo é igual a:", area)

#exercício 2
salario = float(input("Digite o valor do seu salário: "))
salarioCom = salario * 1.05

print("Seu salário total com comissão é: ", salarioCom)

#exercício 3
distancia = float(input("Digite a distância entre as duas cidades em quilômetros: "))
tempo = float(input("Digite o tempo de viagem em horas: "))
vm = distancia / tempo

print(f"A velocidade média do carro foi ou será: {vm} Km/h")

#exercício 4
import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b * b) -( 4 * a * c)
x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)

print("O resultado do X¹ é igual a: ", x1)
print("O resultado do X² é igual a: ", x2)

#exercício 5
dolar = float(input("Digite o valor da cotação do dolar atual: "))
valor = float(input("Insira o valor a ser convertido: "))
valorConv = dolar * valor

print(f"O valor convertido é igual a: R${valorConv}")

#exercício 6
print("Bem-vindo ao restaurante ComaBem")

conta = float(input("Digite o valor da conta: "))
total = conta * 1.1

print("O valor total da conta considerando a comissão do garçom é igual a: ", round(total,2))

#exercicio 7
from sqlite3 import TimestampFromTicks


temp = float(input("Digite a temperatura em graus Celsius: "))
tempF = 1.8 * temp + 32
tempK = temp + 273

print(f"A temperatura é equivalente a: {round(tempF,2)} °F")
print(f"e também é equivalente a: {round(tempK,2)} °K")