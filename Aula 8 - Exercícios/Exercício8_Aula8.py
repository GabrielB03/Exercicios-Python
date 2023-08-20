tempI = (float(input('Digite a temperatura inicial em °C: ')))
tempF = (float(input('Digite a temperatura final em °C: ')))

tC = tempF - tempI
tempF = tC * 1.8

print(f'Variação da temperatura em °C = {tC}°C')
print(f'Variação da temperatura em °F = {tempF}°F')