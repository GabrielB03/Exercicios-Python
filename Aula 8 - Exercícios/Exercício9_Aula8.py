soma = 0
maior_altura = 0
maior_nome=0

for cont in range(0, 10):
    nome = input('Digite o nome do aluno: ')
    altura = int(input(f'Digite a altura do aluno {nome} em cm: '))
    if cont == 0:
        maior_altura = altura
        maior_nome = nome
    elif altura > maior_altura:
        maior_altura = altura
        maior_nome = nome
    soma += altura

print(f'''Aluno mais alto: {maior_nome} com {maior_altura:.2f} cm de altura.
Média das alturas da turma: {soma / 10:.2f} cm de altura.''')