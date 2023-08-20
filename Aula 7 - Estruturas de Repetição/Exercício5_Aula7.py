masc = 0
fem = 0
contadorM = 0
contadorF = 0

while True:
    sexo = input('Digite o sexo da pessoa: ')
    altura = float(input('Digite a altura da pessoa em metros (0 pra sair): '))
    if altura == 0: break
    elif sexo in 'mM':
        masc = masc + altura
        contadorM += 1
    elif sexo in 'fF':
        fem += altura
        contadorF += 1
    else: print('Sexo inválido!')
    
mediaM = masc/contadorM
mediaF = fem/contadorF
print(f'Média das alturas: \nMasculino: {mediaM:.2f} \nFeminino: {mediaF:.2f}')