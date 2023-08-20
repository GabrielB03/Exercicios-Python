x = []
y = []

for i in range(5):
    x.append(int(input('Digite os valores da primeira lista: ')))
print()
for i in range(5):
    y.append(int(input('Digite os valores da segunda lista: ')))
print()
um_elemento_comum = False

for i in range(len(x)):

    for j in range(len(y)):
        if(x[i] == y[j]):
            um_elemento_comum = True
            print(str(x[i]))

if not um_elemento_comum:
    print('Não há um elemento em comum.')