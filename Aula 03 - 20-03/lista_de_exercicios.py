
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

#6
altura = float(input("Diga sua altura:\n->"))
sexo = input("Diga seu sexo:\n1:femenino\n2:masculino\n->")
if sexo == '1:masculino':
    print(f"seu peso ideal deve ser de {72.7*altura-58}")
else:
    print(f"seu peso ideal deve ser {62.1*altura-44.7}")

#7,8
import math
raiz = math.sqrt(3)
lados = int(input("Quantos lados possuem o poligono?:\n->"))
medida = int(input("Qual o tamanho do lado em cm?:\n->"))
if lados == 3:
    print(f"A forma e o TRIANGULO e sua area mede {raiz*medida*medida/4} cm²")
elif lados == 4:
    print(f"A forma e o QUADRADO e sua area mede {4*medida} cm²")
elif lados == 5:
    print(f"A forma e o PENTAGONO e sua area mede {5*raiz*medida*medida/4} cm²")
elif lados < 3:
    print("Nao e um poligono!")
else:
    print("Poligono nao identeficado!")

#9
valor1 = int(input("Digite o primeiro valor:\n->"))
valor2 = int(input("Digite o segundo valor:\n->"))
valor3 = int(input("Digite o terceiro valor:\n->"))
if valor1 > valor2 and valor1 > valor3:
    print(valor1)
elif valor2 > valor1 and valor2 > valor3:
    print(valor2)
else:
    print(valor3)

#10
lado = int(input("Digite o a medida de um lado!:\n->"))
lado2 = int(input("Digite o a medida de outro lado!:\n->"))
lado3 = int(input("Digite o a medida de outro lado!:\n->"))
if lado == lado2 == lado3:
    print("Triangulo Equilatero!")
elif lado != lado2 != lado3 != lado:
    print("Triangulo Escaleno!")
else:
    print("Triangulo Isoscele")

#11
angulo = int(input("Digite o a medida de um angulo do triangulo!:\n->"))
angulo2 = int(input("Digite o a medida de outro angulo do triangulo!:\n->"))
angulo3 = int(input("Digite o a medida de outro angulo do triangulo!:\n->"))
if angulo > 90 or angulo2 > 90 or angulo3 > 90:
    print("Triângulo Obtusângulo")
elif angulo == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triangulo Retangulo")
else:
    print("Triangulo Acutangulo")
'''

