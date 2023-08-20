lista=[]
for i in range (10):
    val = int(input('Digite o valor: '))
    lista.append(val)

mSalario = max(lista)
print(f'O maior salário é de: R${mSalario}')

soma = sum(lista)

media = soma / len(lista)

acima = 0
baixo = 0

for valor_media in lista:
    if valor_media <850:
        baixo += 1

print(f'A média dos salários é de: {media:.2f}')
print(f'\nQuantidade de valores abaixo de R$850: {baixo}')