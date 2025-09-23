acougue = {
    'Carnes' : ['Patinho', 'Coxão Mole', 'Picanha', 'Maminha', 'Linguiça'],
    'R$/Kg' : [35.90, 49.90, 39.90, 80, 45.90, 15],
    'estoque' : [10,50,30,15,20,100],
    'Validade' : ['4', '7', '5', '9', '20','50']
}


def add_prod():
    for key in acougue.keys():
        info = input(f'Diga o novo {key}: ')
        acougue[key].append(info)

def rem_prod():
    produto = input("Digite o nome do produto que deseja remover: ")
    if produto in acougue['Carnes']:
        idx = acougue['Carnes'].index(produto)
        for key in acougue.keys():
            acougue[key].pop(idx)
        print(acougue)

acao = input('Qual ação voce deseja fazer?\n-Adicionar item \n-Remover item \n-Alterar Informação \n->')

if acao == 'Adicionar produto':
    add_prod()

elif acao == 'Remover item':
    rem_prod()