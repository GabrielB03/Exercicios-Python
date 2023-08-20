valorPrestacao = float(input('Digite o valor da prestação: '))
multa = float(input('Digite a porcentagem da multa pelo atraso: '))
dias = int(input('Digite a quantidade de dias de atraso: '))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*dias)

print(f'O valor da prestação de atraso é igual a R$ {prestacao}')