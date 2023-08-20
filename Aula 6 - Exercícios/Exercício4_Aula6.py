#Entrada
h = float(input('Digite a sua altura: '))
sexo = input('Digite o seu sexo(M|F): ')

#Processamento
if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7*h) - 58
elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1*h) - 44.7

#Saída
print(f'O peso ideal dessa pessoa é {pesoIdeal:.2f}')