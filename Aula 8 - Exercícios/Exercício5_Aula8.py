import math
soma = 0
n = int(input('Digite a quantidade de turmas: '))
for i in range (n):
    num = int(input(f'Digite a quantidade de alunos da {i+1}ª turma: '))
    soma += num
media = math.ceil(soma/n)
print(f'As turmas tem em média {media:.0f} alunos')