#Entrada
nome = (input('\nQual o seu nome?: '))
horas = float(input('Que horas são (0-23)?'))

#Saída
if (horas >= 5 and horas < 12):
    print(f'Bom dia', nome)
elif (horas >= 13 and horas < 18):
    print(f'Boa tarde', nome)
else:
    print(f'Boa noite', nome)