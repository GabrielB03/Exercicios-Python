import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b * b) -( 4 * a * c)
x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)

print("O resultado do X¹ é igual a: ", x1)
print("O resultado do X² é igual a: ", x2)