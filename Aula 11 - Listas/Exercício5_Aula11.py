nomes = []
notas = []
cursos = []
tads = 0
quant = 0

while True:
    nome = input('Digite o nome do aluno (vazio pra sair): ')
    if nome == '':
        break
    nomes.append(nome)
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
    if nota > 5:
        quant += 1
    curso = int(input('Digite o curso do aluno [1 para CCP / 2 para TADS]'))
    if curso == 1:
        cursos.append('CCP')
    else:
        cursos.append('TADS')
        tads += 1

print(f'''Quantidade de alunos em TADS: {tads}
Média das notas dos {len(notas)} alunos: {sum(notas)/len(notas):.2f}
Alunos acima da média: {quant}''')