import main
import verificadores
import produtos
import clientes
import categorias

from datetime import datetime

def informar_cliente():
    login_cliente = input("Deseja logar como cliente?\n"
                          "Informe seu CPF:\n")

    login = clientes.verifica_cpf_login(login_cliente)

    if login == True:
        print(f"Cliente logado: {login_cliente}")
        return login_cliente
    else:
        print("Cpf nao localizado!")
        return False


def carrinho_adicionar():
    cod = ""
    produtos.listar_produtos()
    while True:
        main.carrinho_compras.append(input("Digite o codigo do produto desejado.\n"))
        cod = input("Deseja adicionar mais algum produto? Digite S, ou qualquer outro character para sair.\n")
        if cod == "S":
            pass
        else:
            break


def carrinho_remover():
    main.produtos_no_carrinho.clear()
    cod = ""
    print("PRODUTOS NO CARRINHO: ")

    with open("produtos.txt", "r") as file:
        for produtos_arquivo in file:
            main.produtos_no_carrinho.append(produtos_arquivo.strip())

    for item in main.carrinho_compras:
        for prod in range(len(main.produtos_no_carrinho)):
            try:
                cod_prod = main.produtos_no_carrinho[prod].split(",")[0]
                prod_nome = main.produtos_no_carrinho[prod].split(",")[1]
                prod_preco = main.produtos_no_carrinho[prod].split(",")[2]
                cat_produto = main.produtos_no_carrinho[prod].split(",")[3]

                if item == cod_prod:
                    print(f"{main.produtos_no_carrinho[prod]}")
            except:
                pass
    while True:
        #CODIGO DO ITEM
        valida_campo = False
        while True:
            item_a_remover = input("\nDigite o codigo do produto a ser removido do carrinho (ou N para sair): \n")

            if len(item_a_remover) == 0:
                print("Valor em branco, por favor digite um codigo valido.\n")
            elif item_a_remover == 'N':
                break
            elif item_a_remover in main.carrinho_compras:
                valida_campo = verificadores.verifica_campo_numerico(item_a_remover)
                main.carrinho_compras.remove(item_a_remover)
            if valida_campo == True:
                break
        if item_a_remover == 'N':
            break
        else:
            cod = input("Deseja cancelar mais algum produto? Digite S, ou qualquer outro character para sair.\n")
            if cod == "S":
                pass
            else:
                break


def listar_produtos_categoria():
    categorias.listar_categorias()
    cat = input("Informe a categoria: \n")

    print(f"Lista de categorias:\n")

    with open("produtos.txt", "r") as file:
        for produtos_arquivo in file:
            main.produtos_categoria.append(produtos_arquivo.strip())

    try:
        for prod in range(len(main.produtos_categoria)):
            cat_produto = main.produtos_categoria[prod].split(",")[3]
            if cat == cat_produto:
                print(main.produtos_categoria[prod])
    except:
        pass

    return main.produtos_categoria


def finalizar_carrinho():
    car_products = ""
    pre_produto = float("0.00")
    pre = 0
    npdt = ""
    vpdt = 0
    valor_compra = 0

    main.produtos_no_carrinho.clear()

    if len(main.carrinho_compras) > 0:
        with open("produtos.txt", "r") as file:
            for produto in file:
                main.produtos_no_carrinho.append(produto.strip())

        print(f"ITEM    |   PRECO")
        try:
            for codigos in main.carrinho_compras:
                for prod in range(len(main.produtos_no_carrinho)):
                    cpdt = main.produtos_no_carrinho[prod].split(",")[0]
                    if codigos == cpdt:
                        pre_produto = float(pre_produto) + float(main.produtos_no_carrinho[prod].split(",")[2])
                        npdt = main.produtos_no_carrinho[prod].split(",")[1]
                        vpdt = float(main.produtos_no_carrinho[prod].split(",")[2])
                        print(f"{npdt}    |    R${vpdt}")
        except:
            pass

        valor_total = pre_produto
        print(f"\nValor total da compra: R${str(valor_total)}\n")

        modalidade_pagamento = int(input("Insira a modalidade de pagamento:\n"
                                         "1. Dinheiro\n"
                                         "2. Cartão\n"
                                         "3. Voltar\n"))

        if modalidade_pagamento == 1:
            # NOVO PREÇO
            valida_campo = False
            while True:
                dinheiro_recebido = input("Informe a quantia paga pelo cliente: \n")
                valida_campo = verificadores.verifica_campo_float(dinheiro_recebido)
                if valida_campo == True:
                    dinheiro_recebido = float(dinheiro_recebido)
                    break

            if dinheiro_recebido >= valor_total:
                print(f"Troco: R${dinheiro_recebido - valor_total}\n")

                data_atual = datetime.now()
                data_atual = data_atual.strftime("%Y-%m-%d")

                hora_agora = datetime.now()
                hora_agora = hora_agora.strftime("%Y-%m-%d %H:%M:%S")

                for codigos in main.carrinho_compras:
                    car_products = f"{car_products}{codigos};"

                with open("vendas.txt", "a") as file:
                    file.write(f"{hora_agora},{valor_total},{car_products}\n")
                print(f"Compra efetuada: {hora_agora},{valor_total},{car_products}")

                main.carrinho_compras.clear()
                car_products = ""
            else:
                print(f"Valor insuficiente! Valor da compra: {valor_total}, valor pago: {dinheiro_recebido}\n")
                car_products = ""
                npdt = ""
                vpdt = 0



        elif modalidade_pagamento == 2:
            cartoes = []
            numeros_cartoes = []
            senhas_cartoes = []
            validades_cartoes = []
            saldo_cartoes = []

            while True:
                card = input("Insira o numero do cartão:\n")
                valida_campo = verificadores.verifica_campo_numerico(card)
                if valida_campo == True:
                    break

            while True:
                senha = input("Insira sua senha:\n")
                valida_campo = verificadores.verifica_campo_numerico(senha)
                if valida_campo == True:
                    break

            with open("credit_cards.txt", "r") as file:
                for cartao in file:
                    cartoes.append(cartao.strip())

            for cod_cartao in range(len(cartoes)):
                c = cartoes[cod_cartao].split(",")[0]
                s = cartoes[cod_cartao].split(",")[1]
                d = cartoes[cod_cartao].split(",")[2]
                a = cartoes[cod_cartao].split(",")[3]
                numeros_cartoes.append(c)
                senhas_cartoes.append(s)
                validades_cartoes.append(d)
                saldo_cartoes.append(a)

            data_atual = datetime.now()
            data_atual = data_atual.strftime("%Y-%m-%d")

            hora_agora = datetime.now()
            hora_agora = hora_agora.strftime("%Y-%m-%d %H:%M:%S")

            idx = 0

            if card in numeros_cartoes and senha in senhas_cartoes:
                for asd in range(len(numeros_cartoes)):
                    if card == numeros_cartoes[asd]:
                        idx = int(asd)

                cartao_validade = validades_cartoes[idx]
                if data_atual <= cartao_validade:
                    saldo_total = saldo_cartoes[idx]
                    if valor_total < float(saldo_total):
                        novo_saldo_cartao = float(saldo_total) - float(valor_total)
                        print(f"Saldo restante: R${novo_saldo_cartao}\n")

                        for codigos in main.carrinho_compras:
                            car_products = f"{car_products}{codigos};"

                        with open("vendas.txt", "a") as file:
                            file.write(f"{hora_agora},{valor_total},{car_products}\n")
                        print(f"Compra efetuada: {hora_agora},{valor_total},{car_products}")

                        with open("credit_cards.txt", "w") as file:
                            cartoes.remove(f"{card},{senha},{cartao_validade},{saldo_total}")
                            cartoes.append(f"{card},{senha},{cartao_validade},{novo_saldo_cartao}")
                            for t in cartoes:
                                file.write(f"{t}\n")

                        main.carrinho_compras.clear()
                        car_products = ""
                    else:
                        print(f"Saldo insuficiente, saldo: {saldo_total}")
                        car_products = ""
                else:
                    print(f"Data validade do cartão: {cartao_validade} menor que a data atual: {data_atual}.")
                    car_products = ""

        elif modalidade_pagamento == 3:
            return print("Pagamento Cancelado!")


    else:
        return print("Carrinho vazio!")


def listar_vendas():
    print(f"Lista de vendas: \n")
    with open("vendas.txt", "r") as file:
        for i in file:
            print(i.strip())
            print("-----------------")