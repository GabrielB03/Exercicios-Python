contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
num = 0
while num != -1:
    num = int(input('Digite um número inteiro entre 0 e 100 (Digite -1 para sair): '))
    if num >=0 and num <=25: contador1 += 1
    elif num <=50: contador2 += 1
    elif num <=75: contador3 += 1
    elif num <=100: contador4 += 1
    else: break
print(f'[0-25]: {contador1}')
print(f'[26-50]: {contador2}')
print(f'[51-75]: {contador3}')
print(f'[76-100]: {contador4}')