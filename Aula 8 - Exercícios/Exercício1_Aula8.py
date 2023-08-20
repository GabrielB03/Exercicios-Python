contadorCarneiro = 0

while True:
    resp = input('Você já dormiu S/N?: ')
    if resp in 'nN':
         contadorCarneiro += 1
    else: break

print(f'Você contou {contadorCarneiro} carneirinhos!')