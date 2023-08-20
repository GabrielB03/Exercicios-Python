#Exercício 2

import math

a = float(input('Digite o valor inteiro de A: '))
b = float(input('Digite o valor inteiro de B: '))
c = float(input('Digite o valor inteiro de C: '))
d = (b*b) - (4*a*c)

if a== 0:
    print("Não é uma equação do segundo grau")
elif d >=0:
    delta = math.sqrt(d)
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)

    print("O resultado do X¹ é igual a: ", x1)
    print("O resultado do X² é igual a: ", x2)

else:
    print("Não há raízes reais")