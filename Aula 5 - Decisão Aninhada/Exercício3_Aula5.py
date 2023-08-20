#Exercício 3

prod = input("Digite o nome do produto: ")
valorC = float(input("Digite o valor da compra: "))

if valorC < 10:
    valorV = valorC/0.30
    print(f"O valor da venda de {prod} será R$ {valorV:.2f}")
elif valorC >= 10 and valorC < 30:
    valorV = valorC/0.50
    print(f"O valor da venda de {prod} será R${valorV:.2f}")
elif valorC >= 30 and valorC < 50:
    valorV = valorC/0.60
    print(f"O valor da venda de {prod} será R${valorV:.2f}")
elif valorC >= 50:
    valorV = valorC/0.70
    print(f"O valor da venda de {prod} será R${valorV:.2f}")