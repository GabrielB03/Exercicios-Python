arq = input('Digite o tamanho do arquivo em MB: ')
vel = input('Digite a velocidade do link de internet (Mbps): ')
tempo = arq / vel
min = tempo // 60
seg = tempo % 60
print(f'Tempo aproximado para download: {min} minutos e {seg} segundos.')