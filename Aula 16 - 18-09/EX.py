import pandas as pd
import requests

acougue = {
    'Carnes' : ['Patinho', 'Coxão Mole','Fraldinha', 'Picanha', 'Maminha', 'Linguiça'],
    'Preço' : [35.90, 49.90, 39.90, 80, 45.90, 15],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4', '7', '5', '9', '20','50']
}


def add_prod():
    global indices
    for key in acougue.keys():
        info = input(f'Diga o novo {key}: ')
        acougue[key].append(info)
    indices = cria_indices()
    print(pd.DataFrame(acougue))
    return

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes}\n->")
    while not opcao in lista_opcoes:
        print("Invalido!")
        opcao = input(f"{msg}\n{opcoes}\n->")
    return opcao


def cria_indices():
    #indices = {acougue['Carnes'[i] : i for i in range(len(acougue['Carnes']))]}
    indices = {}
    for i in range(len(acougue['Carnes'])):
        indices[acougue['Carnes'][i]] = i
    return indices


def rem_prod():
    global indices
    item = forca_opcao("Qual item será removido?", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        acougue[key].pop(indice_item)
    print(pd.DataFrame(acougue))
    indices = cria_indices()
    return

def atualizar():
        item = forca_opcao("Qual item você deseja atualizar?", acougue['Carnes'])
        indice_item = indices[item]
        keys = list(acougue.keys())
        keys.pop(0)
        for key in keys:
            if forca_opcao(f"Você quer atualizar {key} para {item}", ['sim','não']) == 'sim':
                info = input(f"Diga o novo {key}: ")
                acougue[key][indice_item] = info
        print(pd.DataFrame(acougue))
        return

def verificar_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def comprar():
    item = forca_opcao("Qual item você quer comprar", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f"{key} : {acougue[key][indice_item]}")
    continuar = forca_opcao(f"Você quer levar {item}?", ["sim", "não"])
    if continuar == "não":
        return
    qtd = verificar_numero(f"Quantos kg de {item}? ")
    carrinho["Valor Total"] += qtd*acougue["Preço"][indice_item]
    if qtd <= acougue["Estoque"][indice_item]:
        acougue["Estoque"][indice_item] -= qtd
        carrinho["Valor Total"] += qtd*acougue["Preço"][indice_item]
        if item not in carrinho["Itens"].keys():
            carrinho["Itens"][item] = qtd
        else:
            carrinho["Itens"][item] += qtd
    else:
        print(f"Só há {acougue["Estoque"][indice_item]}kg no estoque!")
        comprar()

indices = cria_indices()
carrinho = {
    "Endereço" : {
        "Rua" : "",
        "Bairro" : "",
        "N°" : "",
        "CEP" : ""
    },
    "Itens" : {},
    "Valor Total" : 0
}

def cadastro_endereco():
    while True:
        cep = input("Diga seu cep: ")
        endereco = requests.get(f"https://viacep.com.br/ws{cep}/json/")
        if endereco.status_code == 200:
            carrinho["Endereço"] = endereco.json()
            carrinho["Endereco"]["N°"] = input("Número da residencia: ")
            carrinho["Endereço"]["Complemento"] = input("Complemento: ")
            break
        else:
            print("CEP Invalido!")
        return

'''for key in carrinho["Endereço"].keys():
        info = input(f"Diga o/a {key}: ")
        carrinho['Endereço'][key] = info'''


print("Bem vindo à Açougueria Agnello!!")
usuario = forca_opcao("Você é cliente ou funcionario?", ["Cliente","Funcionário"])
while True:
    if usuario == "Funcionário":
        operacao = forca_opcao("Qual operação será realizada?", ["Cadastrar", "Remover", "Atualizar"])
        if operacao == "Cadastrar":
            add_prod()
        elif operacao == "Remover":
            rem_prod()
        else:
            atualizar()
        continuar = forca_opcao("Você deseja realizar outra operação", ["sim", "não"])
        if continuar == "não":
            break
    else:
        cadastro_endereco()
        comprar()
        encerrar = forca_opcao("Encerrar a compra ou ver mais itens? ", ["Encerrar", "Continuar"])
        if encerrar == 'Encerrar':
            print(f"Você vai levar\n {list(carrinho)["Itens"].keys()[0]} na {carrinho["Endereço"]["logradouro"]}")
            print(carrinho)
            break