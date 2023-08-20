from cmath import tan
import math

grau = int(input('Digite o valor em graus para um ângulo: '))
radiano = grau * (math.pi/180)
sen = math.sin(radiano)
coss = math.cos(radiano)
tang = math.tan(radiano)

print(f'O seno do seu ângulo é: {sen:.4f}')
print(f'O cosseno do seu ângulo é: {coss:.4f}')
print(f'A tangente do seu ângulo é: {tang:.4f}')