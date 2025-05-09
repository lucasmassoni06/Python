#Lista de exercicio loop
'''
#1

while True:
    num = input("Digite um numero: ")
    if num.isnumeric():
        num = int(num)
        if num < 10 and num > 0:
            print(f"Seu numero e o {num}")
    else:
        input("Digite um numero valido!")

#2
#a

nome = input("Digite seu nome: ")
while len(nome) < 3:
    nome = input("Digite seu nome: ")
print(f"Ola {nome}!")

#b

while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            print(f"Sua idade e de {idade}")
            break
    else:
        idade = input("Digite sua idade: ")

#c

salario = input("Digite seu salario: ")
while not salario.isnumeric():
    salario = input("Digite seu salario: ")
print(f"Seu salario e de {salario} reais!")

#d

sexo = input("Digite seu sexo, `f` ou `m`: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Digite seu sexo, `f` ou `m`: ")
print(sexo)

#e

estado = input("Digite seu estado civil, s,c,v ou d: ")
while estado != 'c' and estado != 's' and estado != 'v' and estado != 'd':
    estado = input("Digite seu estado civil, s,c,v ou d: ")
print(f"Voce esta {estado}")

#3

a = 80
b = 200
i = 0
while a < b:
    a *= 1.03
    b *= 1.015
    i += 1
print(i)

#4

num = input("Digite um numero: ")
i = 1
while i < 5:
    num1 = input("Digite outro numero: ")
    num = int(num)
    num1 = int(num1)
    num = num1 + num
    i += 1
media = num/i
print(media)

#5

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
if num2 > num1:
    while num2 != num1:
        print(num2 - 1)
        num2 = num2 - 1
if num1 > num2:
    while num1 != num2:
        print(num1 - 1)
        num1 = num1 - 1

#6

usuario = input("Digite seu nome de usuario: ")
senha = input("Digite sua senha: ")
while usuario == senha:
    print("Digite uma senha diferente do nome de usuario!")
    usuario = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")
print(f"Seu usuario e {usuario} e sua senha e {senha}")

#7

num = input("A tabuada de que numero voce deseja? ")
i = 1
while i < 11:
    num = int(num)
    print(f"{num} * {i} = {num*i}")
    i += 1

#8

a = 1
b = 1
i = 0
print(a, b, end=" ")
while i < 10:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    i += 1

#9

i = 0
par = 0
impar = 0
while i < 10:
    num = int(input("Digite um numero: "))
    i += 1
    if num % 2 == 0:
        par += 1
    elif num % 2 == 1:
        impar += 1
print(f"Voce acumulou {par} pares e {impar} impares de {i} numeros!")

#10

num = int(input("Digite um numero para descobrir o valor de seu fatorial: "))
i = num
while i > 1:
    i = i - 1
    num = num * i
print(num)

#11

num = int(input("Digite um numero: "))
i = num
num1 = 0
while i > 2:
    i = i - 1
    if num % i == 0:
        num1 += 1
if num1 > 0:
    print("Ele nao e primo!")
else:
    print("Ele e primo")

#12

num = int(input("Selecione quantos numeros voce quer digitar para calcular a media: "))
i = num
soma = 0
while i != 0:
    valor = int(input("Digite um numero: "))
    soma += valor
    i -= 1
print(f"A media e de {soma/num}")

#13

salario = input("Digite o salario: )
ano = 1996
aumento = 1.5

while ano != 2025:
    salario += salario * (aumento/100)
    aumento *= 2
    ano += 1
print(salario)

#14

num = int(input("Digite um numero: "))
while num > 0:
    if num < 26:
        print("Seu numero esta entre 1 e 25")
        num = int(input("Digite um numero: "))
    elif num < 51:
        print("Seu numero esta entre 25 e 50")
        num = int(input("Digite um numero: "))
    elif num < 76:
        print("Seu numero esta entre 50 e 75")
        num = int(input("Digite um numero: "))
    elif num < 101:
        print("Seu numero esta entre 75 e 100")
        num = int(input("Digite um numero: "))
    else:
        print("Seu numero esta fora dos limites")
        num = int(input("Digite um numero: "))
print("Voce digitou um numero negativo!")
'''
#15

candidato1 = "Joao"
candidato2 = "Jose"
candidato3 = "Jonatam"
candidato4 = "Josue"
nulo = "nulo"
branco = "branco"
voto = input(f"Em quem deseja votar:\n"
             f"1 - {candidato1}\n"
             f"2 - {candidato2}\n"
             f"3 - {candidato3}\n"
             f"4 - {candidato4}\n"
             f"5 - {nulo}\n"
             f"6 - {branco}\n")
if voto == '1':
    print(f"Voce votou no {candidato1}")
elif voto == '2':
    print(f"Voce votou no {candidato2}")
elif voto == '3':
    print(f"Voce votou no {candidato3}")
elif voto == '4':
    print(f"Voce votou no {candidato4}")
elif voto == '5':
    print(f"Voce votou no {nulo}")
elif voto == '6':
    print(f"Voce votou no {branco}")