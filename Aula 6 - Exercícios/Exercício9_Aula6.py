#Entrada
num1 = float(input('Digite o 1° número real: '))
num2 = float(input('Digite o 2° número real: '))
print('[1] Média')
print('[2] Diferença maior-menor')
print('[3] Produto')
print('[4] Divisão n1/n2')

#Processamento
nome = input("Digite uma opção: ")
media = (num1 + num2)/2
diferenca = num1 - num2
produto = num1 * num2

#Saída
if (nome == '1'):
    print(f"A média é: {media}")
elif (nome == '2'):
    print(f"A diferença é: {diferenca}")
elif (nome == '3'):
    print(f'O produto é: {produto}')
elif (num2 > 0 or num2< 0 and nome == '4'):
    print('Impossível dividir por zero')
else:
    print('Operação inválida')