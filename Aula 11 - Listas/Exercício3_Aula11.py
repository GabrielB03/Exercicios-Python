placa = []
multa = []
soma = 0

for i in range(5):
    placa = (input(f'Digite o número da placa do {i+1}º carro: '))
    multa = float(input(f'Digite o valor da multa do {i+1}º carro: '))

    if multa >= 300:
        soma += 1

media = multa*2/15

print(f'Valor médio de todas as multas: {media}.')
print(f'Quantos carros possuem o valor de multa maior ou igual a R$300,00: {soma}')