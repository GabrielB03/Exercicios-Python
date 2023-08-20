#Entrada
nota1 = float(input('Digite a primeira nota parcial: '))
nota2 = float(input('Digite a segunda nota parcial: '))

#Processamento
media = (nota1 + nota2)/2

#Saída
if media >=9 and media <10:
    print('Conceito: A\nMensagem: Aprovado')
elif media >= 7.5 and media < 9:
    print('Conceito: B\nMensagem: Aprovado')
elif media >= 6.0 and media < 7:
    print('Conceito: C\nMensagem: Aprovado')
elif media >= 4 and media < 6:
    print('Conceito: D\nMensagem: Reprovado')
else:
    print('Conceito: E\nMensagem: Reprovado')