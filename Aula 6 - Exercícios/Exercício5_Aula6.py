#Entrada
import math
area = float(input('Digite a área pintada em metros: '))

#Processamento
qtdTinta = area/3
qtdLatas = math.ceil(qtdTinta/18)

#Saída
print(f'Você precisará comprar {qtdLatas} latas')
print(f'O valor total a pagar será: R$ ', qtdLatas*80)