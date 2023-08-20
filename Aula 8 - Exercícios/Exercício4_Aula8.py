soma = 0
conta = input('Digite a conta com 4 algarismos: ')
for d in conta:
    soma += int(d)
dig = soma % 10
print(f'Número completo da conta: 00{conta}-{dig}')