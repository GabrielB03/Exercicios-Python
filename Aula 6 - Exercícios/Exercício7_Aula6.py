#Entrada
print('Coordenadas de um ponto P (X, Y)')
x = float(input("Digite a coordenada X: "))
y = float(input("Digite a coordenada Y: "))

#Saída
if x>0 and y>0:
    print('O ponto P pertence ao 1° quadrante')

if x<0 and y>0:
    print('O ponto P pertence ao 2° quadrante')

if x<0 and y<0:
    print('O ponto P pertence ao 3° quadrante')

if x>0 and y<0:
    print('O ponto P pertence ao 4° quadrante')
