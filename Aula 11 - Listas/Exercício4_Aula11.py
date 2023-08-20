dias_semana = list()
qtd_chuva = list()
total_quarta = 0
media = 0
total = 0
i = 0

while i < 10:
    dias_semana.append(input('Informe o dia da semana: '))
    qtd_chuva.append(float(input('Informe a quantidade de chuva: ')))
    i += 1

i = 0
while i < 10:
    total += qtd_chuva[i]
    if dias_semana[i] == 'quarta-feira':
        total_quarta += qtd_chuva[i]

i += 1

media = total_quarta / dias_semana.count('quarta-feira')
print(f'Média total {media:.2f}: ')