#Exercício 1

idade = int(input('Digite a sua idade: '))

if idade <16:
    print('Não-Eleitor')
elif idade >=18 and idade <=65:
    print('Eleitor Obrigatório.')
elif idade <=18 and idade >=16 or idade >65:
    print('Eleitor Facultativo.')