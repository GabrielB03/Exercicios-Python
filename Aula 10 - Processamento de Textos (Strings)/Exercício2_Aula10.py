print("Entrada :")  
num = input("Digite um número inteiro com três algarismos: ")
iNum = num[::-1]
soma = int(iNum) + int(num)

print("\nSaída: ")
print(f"O inverso do número é {iNum} ")
print(f"A soma de {num} + {iNum} = {soma}")