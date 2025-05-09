
'''
#Operadores booleanos: >,<,>=,<=,==,!=
a = 2
b = 3
#print(2>3)
#and, or
print(f"A operacão {a} > {b} and {a} != {b}, ou seja, {a>b}, resulta  {a<b and a!=b}")


idoso = input("Você é idoso??\n->")
cartaozinho = input("Você tem o cartaozinho?\n->")
if idoso == 'sim' and cartaozinho == 'sim'
    print("pode estacionar!")
else:
    print("Não pode!")


idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
    print("Pode estacionar!")
else:
    print("Não pode!")


letra = input("Escreva uma letra:\n->")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("É uma vogal!")
else:
    print("É uma consoante!")

#elif = é um if porem se der verdadeiro ele não tenta as seguintes
time =input("Pra que time você torce?:\n->")
if time == 'Corinthians':
    print("É o maior do Brasil!")
elif time == 'Palmeiras':
    print("Coitado")
elif time == 'São Paulo':
    print("Coitado")
else:
    print("Mais coitado ainda")

#Imposto de renda
salario = int(input("Digite o seu salário:\n->"))
if salario < 1904:
    print("Não há imposto!")
elif salario >= 1904 and salario < 2827:
    imposto = 0.075
    print(f"O seu salario é de {salario} e o imposto será de 7,5%, sendo assim terá que pagar {salario * imposto}")
elif salario >= 2827 and salario < 3751:
    imposto = 0.15
    print(f"O seu salario é de {salario} e o imposto será de 15%, sendo assim terá que pagar {salario * imposto}")
elif salario >= 3751 and salario < 4664:
    imposto = 0.225
    print(f"O seu salario é de {salario} e o imposto será de 22,5%, sendo assim terá que pagar {salario * imposto}")
else:
    imposto = 0.275
    print(f"O seu salario é de {salario} e o imposto será de 27,5%, sendo assim terá que pagar {salario * imposto}")


#Calculadora
entrar = input("Você quer fazer contas?\n->")
if entrar == 'sim':
    numero1 = int(input("Digite o primeiro número:\n->"))
    sinal = input("Digite o sinal desejado:\n->")
    numero2 = int(input("Digite o segundo número\n->"))
    if sinal == '+':
        print(f"{numero1 + numero2}")
    elif sinal == '-':
        print(f"{numero1 - numero2}")
    elif sinal == '*':
        print(f"{numero1 * numero2}")
    else:
        print(f"{numero1 / numero2}")
else:
    print("Tchau!!")


#lista de exercicio
#1
valor1 = int(input("Digite o primeiro valor:\n->"))
valor2 = int(input("Digite o segundo valor:\n->"))
if valor1 > valor2:
    print(f"{valor1}")
else:
    print(f"{valor2}")

#2
ano = int(input("Qual ano você nasceu?:\n->"))
if ano <= 2009:
    print("Pode votar esse ano!")
else:
    print("Não pode votar esse ano!")

#3
senha = int(input("Digite sua senha:\n->"))
if senha == 1234:
    print("Acesso Permitido!")
else:
    print("Acesso Negado!")

#4
maca = int(input("Quantas maças você deseja comprar?:\n->"))
if maca < 12:
    print(f"Cada maça custará R$ 0,30, sendo assim o valor total será de {maca*0.30}")
else:
    print(f"Cada maça custará R$ 0,25, sendo assim o valor total será de {maca*0.25}")

#5
valor1 = int(input("Digite o primeiro valor:\n->"))
valor2 = int(input("Digite o segundo valor:\n->"))
valor3 = int(input("Digite o terceiro valor:\n->"))
if valor1 > valor2:
    if valor2 > valor3:
        print(f"{valor1}>{valor2}>{valor3}")
    elif valor1 < valor3:
        print(f"{valor3}>{valor1}>{valor2}")
    else:
        print(f"{valor1}>{valor3}>{valor2}")

elif valor2 > valor1:
    if valor1 > valor3:
        print(f"{valor2}>{valor1}>{valor3}")
    elif valor2 < valor3:
        print(f"{valor3}>{valor2}>{valor1}")
    else:
        print(f"{valor2}>{valor3}>{valor1}")
'''
#6
