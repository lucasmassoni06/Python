acougue = {
    'carnes' : ['Patinho', 'Coxão Mole', 'Fraldinha', 'Picanha', 'Maminha', 'Linguiçona'],
    'R$/kg' : [35.90,49.90,39.90,80.00,45.90,15],
    'estoque' : [10,50,30,15,20,15],
    'validade' : ['4','7','5','9','20','50']
}


def adicionar_produto():
    for key in acougue.keys():
        info = input(f'Diga o novo {key}: ')
        acougue[key].append(info)

def remover_produto():
    info = input('Diga qual produto deseja remover? ')
    for i in range(len(acougue['carnes'])):
        if info == acougue['carnes']:
            indice = i
    for key in acougue.keys():
        acougue[key].pop(indice)
    print(acougue)

print(acougue)
acao = input("O que você deseja fazer? \n-Adicionar item\n-Remover item\n-Alterar item\n-Informação\n")

if acao == 'Adicionar Item':
    adicionar_produto()

elif acao == 'Remover item':
    remover_produto()
