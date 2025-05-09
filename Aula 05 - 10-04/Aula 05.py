'''
i = 0
pares = 0
num = int(input(f"Diga o {i+1}º número:"))
if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
i = i + 1
num = int(input(f"Diga o {i+1}° número:"))
if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
i = i + 1
num = int(input(f"Diga o {i+1}° número:"))
if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
i = i + 1
num = int(input(f"Diga o {i+1}° número:"))
if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
i = i + 1
num = int(input(f"Diga o {i+1}° número:"))
if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
i = i + 1

print(f"Você digitou {pares} números pares e {i - pares} números impares")

#mesma coisa só que com while

i = 0
pares = 0

while i < 5:
    num = int(input(f"Diga o {i+1}º número: "))
    if num%2 == 0:
        pares = pares + 1
    i= i + 1
print(f"Você digitou {pares} número pares e {i - pares} números impares")

#while para senha

senha = int(input("Digite a sua senha: "))
while senha != 1234:
    senha = int(input("Senha incorreta, Digite novamente: "))
print("Senha correta!")

#while com limite de rep

senhacorreta = '1234'
i = 0
senha = input("Digite sua senha!")
while senha != senhacorreta and i < 2:
    senha = input(f"Senha incorreta,você tem {2 - i} tentativas, Digite novamente: ")
    i = i + 1
if senha == senhacorreta:
    print("Acesso liberado!")
else:
    print("Bloqueado!")

#usar while para obrigar o usuario a preencher correto

sexo = input("Qual é o seu sexo?\n-feminino\n-masculino\n->")
while sexo != 'feminino' and sexo != 'masculino':
    sexo = input("Digite um sexo válido:")
print(f"Olá seu sexo é {sexo}!")

#metodo com or

sexo = input("Qual é o seu sexo?\n-feminino\n-masculino\n->")
while not (sexo == 'feminino' or sexo == 'masculino'):
    sexo = input("Digite um sexo válido:")
print(f"Olá seu sexo é {sexo}!")

#verificar se o digitado é número

idade = input("Diga sau idade: ")
while idade.isnumeric() == False:
    idade = input("Digite uma idade válida!\n-")
print(f"Sua idade é: {idade}")
'''