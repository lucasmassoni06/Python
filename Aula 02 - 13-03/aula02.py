'''
palavra_1 = "Olá"
palavra_2 = "Mundo"
print(palavra_1 + " " + palavra_2)
frase = (palavra_1 + " " + palavra_2)
print(frase)

frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Lucas"
print(frase)

frase = input ("Diga a primeira frase: ")
print(frase)
frase = frase + " " + input ("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input ("Diga a terceira palavra: ")
print(frase)

a = 2
b = 3
print(a+b)
soma = (3+2)
print(soma)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(f"a soma entre {a} e {b} é {soma}")


Nome = input("Diga seu nome: ")
print("Bem vindo a calculadora")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = (a+b)
sub = (a-b)
mult = (a*b)
div = (a/b)
print(f"a soma entre {a} e {b} é: {soma}")
print(f"a subtração entre {a} e {b} é: {sub}")
print(f"a multiplicação entre {a} e {b} é: {mult}")
print(f"a divisão entre {a} e {b} é: {div}")


a=3
b=2
print(f"O resultado de {a} > {b} é {a>b}")
print(f"O resultado de {a} >= {b} é {a>=b}")
print(f"O resultado de {a} < {b} é {a<b}")
print(f"O resultado de {a} <= {b} é {a<=b}")
print(f"O resultado de {a} == {b} é {a==b}")
print(f"O resultado de {a} != {b} é {a!=b}")

a = 2
b = 3
print(f"{a} != {b} and {a} < {b}, ou seja, {2 != 3} and {3 > 2} dá {2 != 3 and 3 > 2}")
print(f"{a} == {b} and {a} != {b}, ou seja, {2 == 3} and {3 != 2} dá {2 == 3 and 3 != 2}")
print(f"{a} != {b} and {a} > {b}, ou seja, {2 != 3} and {3 < 2} dá {2 != 3 and 3 < 2}")
print(f"{a} > {b} and {a} == {b}, ou seja, {2 > 3} and {3 == 2} dá {2 > 3 and 3 == 2}")

a = 2
b = 3
print(f"{a} != {b} or {a} < {b}, ou seja, {2 != 3} and {3 > 2} dá {2 == 3 or 3 > 2}")
print(f"{a} == {b} or {a} < {b}, ou seja, {2 == 3} and {3 > 2} dá {2 == 3 or 3 > 2}")
print(f"{a} != {b} or {a} > {b}, ou seja, {2 != 3} and {3 < 2} dá {2 != 3 or 3 < 2}")
print(f"{a} == {b} or {a} > {b}, ou seja, {2 == 3} and {3 < 2} dá {2 == 3 or 3 < 2}")

idade = int(input("diga sua idade: "))
if idade >= 18:
    print("liberado😊")
if idade < 18:
    print("Recusado😒")

idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
    print("Estacione aqui!")
else:
    print("Não pare aqui!")
'''
idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
    cartao = input("Você tem o cartão?:\n->")
    if cartao == 'sim':
        print("Pode estacionar aqui!")
    else:
        print("Não pare aqui!")
else:
    print("Não pare aqui!")