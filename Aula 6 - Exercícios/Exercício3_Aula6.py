#Entrada
num = int(input('Digite um número inteiro: '))

#Processamento
if num > 0:
    res = 'Positivo'
elif num < 0:
    res = 'Negativo'
else:
    res = 'Nulo'

#Saída
print(f'O número {num} é {res}')