#Entrada
seg = int(input('Digite a quantidade de segundos: '))

#Processamento
horas = seg // 3600
min = seg%3600//60
seg = seg%60

#Saída
print(horas, 'horas', min, 'minutos', seg, 'segundos')