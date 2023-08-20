#Exercício 4
agua = float(input('Digite o valor da sua conta de água: '))
luz = float(input('Digite o valor da sua conta de luz: '))
telefone = float(input('Digite o valor da sua conta de telefone: '))
salario = float(input('Digite o valor do seu salário: '))

contas = agua+luz+telefone
sobra = salario-contas

if salario<contas:
    print('Seu salário é insuficiente')
else:
    print(f'Seu salário é suficiente, ainda sobra: {sobra:.2f}')