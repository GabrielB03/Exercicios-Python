#Exercício 3
compra = float(input('Digite o valor da sua compra: '))

if compra >= 200:
    desconto = compra*0.2
else:
    desconto = 0
    
print("Valor a pagar R$ ", compra-desconto)