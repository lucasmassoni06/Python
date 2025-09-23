'''
#FOR

vogais = 0
for char in 'danilo':
    if char in ['a','e','i','o','u']:
        vogais += 1
print(vogais)



lista = (3, True, 7.2, 'nome', [])
for elem in lista:
    print(elem)

for i in range (len(lista)):
    lista[i] += 1
print(lista)




numeros = [5,1,7,9,0,2]
soma = 0
for num in numeros:
    soma += num
print(soma)

soma = 0
for i in range (len(numeros)):
    soma += numeros[i]




alunos = ['Lucas Sena', 'Vinicius', 'Matheus Santos', 'Leandro Afonso']
notas = [2,6,8,5]

for i in range (len(notas)):
    if notas[i] >= 6:
        print(f'O {alunos[i]} passou com {notas[i]}')

#FUNCAO

def verifica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

qtd = verifica_numero('Quantos numeros voce vai colocar na lista? ')

lista = []
while len(lista) < qtd:
    num = verifica_numero(f'Diga o {len(lista)} numeros: ')
    lista.append(num)
    print(lista)



def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in lista_opcoes:
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

vinhos = ['Pergola', 'Sangue de Boi', 'Salton']
vinho = forca_opcao('Qual vinho voce quer: ',vinhos)
opcoes = ['s','n']
continuar = forca_opcao('Voce quer continuar? (s/n)',opcoes)
print(f'Voce disse {continuar}')




#Exercicio

def listas(msg):
    qtd = input(msg)
    while not qtd.isnumeric():
        qtd = input(msg)
    qtd = int(qtd)
    return qtd

qtd = listas('Quantos número voce quer na lista?\n->')
qtd -= 1
lista = []

while not len(lista) > qtd:
    num = listas(f'Fale o {len(lista) + 1} numero da lista:')
    lista.append(num)

soma = 0
for number in lista:
    soma += number
media = soma/len(lista)
print(f'{media}')





#ACHAR PARES




def contador_pares(lista):
    par = 0
    for numero in lista:
        if numero%2 == 0:
            par += 1
    return par

lista = [5, 8, 6, 0, 1, 3]
print(contador_pares(lista))







#ACHAR O MAIOR



def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

carros = ['up', 'gol', 'polinho turbão manual', 'uno', 'celta']
precos = [10,20,10000,100,200]
indice_maior_preco = acha_maior(precos)
carro_mais_caro = carros[indice_maior_preco]
preco_mais_caro = precos[indice_maior_preco]
print(f'O Carro mais caro é o {carro_mais_caro} e custa {preco_mais_caro}')

'''

#FORCAR A ESCOLHER UM


def join(lista_str,sep):
    ajuntado = lista_str[0]
    for i in range(1,len(lista_str)):
        ajuntado += sep + lista_str[1]
    return ajuntado

def forca_opcao(msg, lista_opcoes):
    #opcoes = '\n'.join(lista_opcoes)
    opcoes = join(lista_opcoes,'\n')
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in lista_opcoes:
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

carros = ['up', 'gol', 'polinho turbão manual', 'uno', 'celta']
precos = [10,20,10000,100,200]


escolha = forca_opcao('Qual carro te interessa?', carros)
for i in range(len(carros)):
    if carros[i] == escolha:
        indice_escolha = i
print(f'O {escolha} custa {precos[indice_escolha]}')

