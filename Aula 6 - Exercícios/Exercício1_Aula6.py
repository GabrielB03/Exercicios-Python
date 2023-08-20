#Entrada
salario = float(input('Digite o seu salário fixo: '))
vendas = float(input('Digite o valor das suas vendas: '))

#Processamento
comissao = vendas*0.04

#Saída
print('Comissão: R$', comissao)
print('Salário final: R$', salario+comissao)