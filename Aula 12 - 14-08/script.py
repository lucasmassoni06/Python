'''lista = [4,1,5,7,3,6,9,2,10,8]
soma = 0
for numero in lista:
    soma += numero
media = soma/len(lista)
print(media)

lista = []
par = 0
impar = 0
for i in range(1,11):
    num = input("Digite um número:")
    lista.append(num)
for i in range(len(lista)):
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"{lista}\nExistem {par} e {impar}")



def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
         num = input(msg)
    return num
qtd = verifica_numero("Qts numeros vc quer na lista\n")
numeros = []

for i in range(qtd):
    num = verifica_numero(f"Diga o {i+1}° numero: ")
    numeros.append(num)

pares = 0
impar = 0
for num in numeros:
    if num%2 == 0:
        pares += 1
impares = len(numeros) - pares
print(f"Na lista {numeros} ha {pares} pares e {impares} impares")'''


endereco = input("Digite seu endereço: ")

ano = input("Quantos anos você tem?")
while not numb.isnumeric():
    ano = input("Quantos anos você tem?")
ano = int(ano)
if ano > 2007:
    quit()

precos = [50, 20, 35, 15]
def forca_opcoes(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    print(precos)
    escolha = input(f'{msg}\n{opcoes}\n')
    while escolha not in lista_opcoes:
        escolha = input('{msg}\n{opcoes}\n')
    return escolha


qtd = input("Quantos vinhos você quer? ")
while not numb.isnumeric():
    qtd = input("Quantos vinhos você quer? ")
qtd = int(qtd)

vinhos = ["branco", "tinto", "rose", "porto"]
vinho = forca_opcoes("Qual vinho você gostaria? ", vinhos)

