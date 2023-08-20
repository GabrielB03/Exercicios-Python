valorHora = float(input('Digite o valor da hora aula: R$'))
cargaSemanal = int(input('Digite a quantidade de horas semanais: '))

salarioBase = valorHora * cargaSemanal * 4.5
adicional = salarioBase * 1/6
salarioFinal = salarioBase + adicional

print(f'Salário final R$ {salarioFinal}')