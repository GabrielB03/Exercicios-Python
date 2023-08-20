lista = []
val = int(input('Digite o valor (-1 pra sair): '))
while (val != -1):
    lista.append(val)
    val = int(input('Digite o valor (-1 pra sair): '))

soma = sum(lista)
print('A soma dos valores é: ', soma)

media = soma / len(lista)

acima = 0

for valor_media in lista:
    if valor_media > media:
        acima += 1

print('A média é: ', media)
print(f'Quantidade de valores acima da média: {acima}')