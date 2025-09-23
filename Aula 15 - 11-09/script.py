'''dic = {'chave' : 'valor'}
print(dic['chave'])
dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = '123'

--------------------------------------------------------------------------------------------------------


import random
saudacoes = {'oi' : ['ola', 'SALVE', 'BÃo UIA','iae'], 'tchau' : ["flw", 'tchau migo', 'bjs', 'ate mais']}
while True:
    resposta = input("Diga oi ou tchau")
    print(random.choice(saudacoes[resposta]))

if resposta == 'oi':
    print("Ola")
else:
    print("flw")


--------------------------------------------------------------------------------------------------------

poligono = input("Selecione o numero de lados de um poligono: ")
dic_poligonos = {'3' : 'Triangulo',
                 '4' : 'Quadrado',
                 '5' : 'Pentagono',
                 '6' : 'Hexagono',
                 '7' : 'Heptagono',
                 '8' : 'Octogono'
}

print(dic_poligonos[poligono])

--------------------------------------------------------------------------------------------------------

emojis = {
    ':)' : '😁',
    ':(' : '😒',
    '<3' : '❤️',
    ':`(' : '😢'
}

texto = 'eu amo python <3'
for key in emojis.keys():
    texto = texto.replace(key, emojis[key])
print(texto)

--------------------------------------------------------------------------------------------------------


numeros = {
    'um' : '1',
    'dois' : '2',
    'tres' : '3',
    'quatro' : '4',
    'cinco' : '5',
    'seis' : '6',
    'sete' : '7',
    'oito' : '8',
    'nove' : '9',
    'zero' : '0'
}

resposta = input("Digite o número que você quer: ")
for key in numeros.keys():
    resposta = resposta.replace(key, numeros[key])
print(resposta)

--------------------------------------------------------------------------------------------------------

dic = {
    'nome' : ['danilo', 'Bernardo', 'Matheus'],
    'idade' : [20, 18, 19]
}

for i in range(len(dic['nome'])):
    for key in dic.keys():
        print(f"{key} : {dic[key][i]}")
    print()
--------------------------------------------------------------------------------------------------------
'''

frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
#print(frase)
frase = frase.lower()
#print(frase)
frase = frase.replace('.','')
#print(frase)
palavras = frase.split(' ')
#print(palavra)

#contador = {
#    'a' : 0,
#    'aranha': 0,
#    'arranha': 0,
#   'rã': 0,
#    'nem': 0
#}

#for i in range(len(palavras)):
#        contador[palavras[i]] += 1
#print(contador)


contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 0
    else:
        contador[palavra] += 1
print(contador)