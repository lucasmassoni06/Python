

'''
matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
for i in matriz:
    for element in i:
        print(element)


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def fazer_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i%2 == 0 and j%2 == 0:
                linha.append(1)
            elif i%2 != 0 and j%2 != 0:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

nova_matriz = fazer_matriz(8,8)
mostra_matriz(nova_matriz)
'''


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def fazer_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
        
        matriz.append(linha)
    return matriz







import matplotlib.pyplot as plt
plt.imshow(nova_matriz, 'hot')
plt.colorbar()
plt.show()
