endereco = input("Boas vindas a Vinheria Agnello!! Para continuar me informe seu endereço:\n->")
ano = int(input("Agora me informe o ano do seu nascimento!\n->"))

if ano <= 2007:
    bebida = input("Para prosseguir qual vinho você deseja comprar, temos as seguintes opções:\n- Vinho tinto: $50,00\n- Vinho branco: $20,00\n- Vinho rose: $15,00\n- Vinho do porto: $25,00\nQual você deseja?->")
    quantidade = int(input("Quantas garrafas você deseja:\n->"))

    if bebida == 'Vinho tinto':
            preco = 50
    elif bebida == 'Vinho branco':
            preco = 20
    elif bebida == 'Vinho rose':
            preco = 15
    else:
            preco = 25

    print(f"Você selecionou o {bebida} e escolheu {quantidade} garrafa/s dela/s, sendo assim o preço ficará de:${preco * quantidade},00")

    if preco * quantidade > 100:
        frete = 0
        print("Você nâo receberá frete pela entrega!")
    else:
        frete = 10
        print("O frete da entrega será de $10,00!")

    print(f"Muito obrigado por comprar com a gente seu pedido ficou de ${preco * quantidade + frete},00, e será entregue no endereço: {endereco} nos próximos dias!")

else:
    print("Nâo é permitido a venda de bebidas para menores!")