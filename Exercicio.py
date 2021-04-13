from datetime import datetime
import cpf_tools as validator
import string

clientesList = []
lista_cadastrados = []
carrinho_compras = []
produtos_categoria = []
produtos_no_carrinho = []
produtos_list = []
categorias_list = []

menu_geral_validos = ['1', '2', '3', '4']
menu_cliente_validos = ['1', '2', '3']
menu_cliente_carrinho_validos = ['1', '2', '3', '4', '5', '6', '7']
menu_produto_validos = ['1', '2', '3', '4', '5', '6', '7', '8']
menu_consulta_validos = ['1', '2', '3']

valor_total = 0
valida_campo = False

symbols = ['!', '@', '#', '$', '%', '^', '&',
           '*', '(', ')', '<', '>', ',', '=',
           '´', '`', '¨', '^', "~", "'", '"',
           "'", "ª", "º", "{", "}", "-", "[",
           "]"]

numeros = '0123456789'
alfabeto = string.ascii_letters

# -------------Verificadores------------------------------


def verifica_campo_float(valor_digitado):
    if len(valor_digitado) == 0:
        print("Digite algum valor!")
        return False
    for caracter in valor_digitado:
        if caracter in symbols:
            print(f"Valor não permitido para o campo, use apenas caracteres válidos. "
                  f"Utilize ponto para numeros decimais.\n")
            return False
        elif caracter in alfabeto:
            print(f"Valor não permitido para o campo, use apenas caracteres válidos. "
                  f"Utilize ponto para numeros decimais.\n")
            return False
        elif valor_digitado == ".":
            print(f"Valor nulo, inform um numero valido!\n")
            return False
    return True


def verifica_campo_string(nome_campo, valor_digitado):
    if len(valor_digitado) == 0:
        print(f"Digite algum valor {nome_campo}!")
        return False
    for caracter in valor_digitado:
        if caracter in symbols:
            print(f"Valor não permitido para o campo, use apenas caracteres válidos.\n")
            return False
    return True


def verifica_campo_numerico(valor_digitado):
    if len(valor_digitado) == 0:
        print("Digite algum valor!")
        return False
    for numero in valor_digitado:
        if numero not in numeros:
            print(f"Valor não permitido para o campo, use apenas numeros.\n")
            return False
    return True

# ------------Funções Clientes---------------------------

#
# def cadastrar_cliente(cpf: str, nome: str, idade: str):
#     with open("clientes.txt", "a") as file:
#         dados = f"{cpf},{nome},{idade}\n"
#         file.write(dados)
#
#
# def listar_clientes():
#     print(f"Lista de clientes: \n")
#     with open("clientes.txt", "r") as file:
#         for i in file:
#             print(i.strip())
#             print("-----------------")
#
#
# def verifica_cpf_login(cpf: str):
#     contador_cpf_validador = 0
#     lista_cadastrados.clear()
#
#     with open("clientes.txt", "r") as file:
#         for i in file:
#             lista_cadastrados.append(i.strip())
#
#     for cli in range(len(lista_cadastrados)):
#         cpf_cadastro = lista_cadastrados[cli].split(",")[0]
#         if cpf == cpf_cadastro:
#             contador_cpf_validador = 1
#
#     if int(contador_cpf_validador) == 1:
#         return True
#     else:
#         return False
#
#
# def verifica_cliente(cpf: str):
#     contador_validador = 0
#     lista_cadastrados.clear()
#     with open("clientes.txt", "r") as file:
#         for i in file:
#             lista_cadastrados.append(i.strip())
#
#     for cli in range(len(lista_cadastrados)):
#         cpf_cadastro = lista_cadastrados[cli].split(",")[0]
#         if cpf == cpf_cadastro:
#             contador_validador = 1
#
#     cpf_valido = validator.cpf_str_validation(cpf)
#
#     if cpf_valido == False and int(contador_validador) == 0:
#         contador_validador = 2
#
#     if int(contador_validador) == 0:
#         return True
#     elif int(contador_validador) == 1:
#         print("CPF já existe um cadastro desse cpf.\n")
#         return False
#     elif int(contador_validador) == 2:
#         print("CPF inválido\n")
#         return False


# ------------Funções Produtos---------------------------

def cadastrar_produto(codigo: str, nome: str, preco: str, categoria: str):
    produtos_list.clear()
    categorias_list.clear()
    temp_prod_codigo = []

    with open("produtos.txt", "r") as file:
        for i in file:
            produtos_list.append(i.strip())

    for prod in range(len(produtos_list)):
        p = produtos_list[prod].split(",")[0]
        temp_prod_codigo.append(p)

    if codigo not in temp_prod_codigo:

        with open("categorias.txt", "r") as file:
            for i in file:
                categorias_list.append(i.strip())

        if categoria in categorias_list:
            with open("produtos.txt", "a") as file:
                dados = f"{codigo},{nome},{preco},{categoria}\n"
                file.write(dados)
                print(f"Produto cadastrado com sucesso! "
                      f"{dados}\n")
        else:
            print("Categoria não localizada!")
    else:
        print("Já existe um produto cadastrado com este codigo")


def listar_produtos():
    produtos_list.clear()
    print(f"Lista de produtos: \n")
    with open("produtos.txt", "r") as file:
        for i in file:
            print(i.strip())
            produtos_list.append(i.strip())
            print("-----------------")


def alterar_produto(codigo):
    produtos = []
    contador = 0

    produtos.clear()

    with open("produtos.txt", "r") as file:
        codigoInserido = codigo

        # Puxa informações do file.txt e da append na list
        for i in file:
            produtos.append(i.strip())

        # Busca o produto pelo codigo, e pede informações para serem alteradas
        for produto in range(len(produtos)):
            cod = produtos[produto].split(",")[0]
            if codigoInserido == cod:
                contador = 1

                #NOVO NOME
                valida_campo = False
                while True:
                    novo_nome = input("Digite o novo nome do produto: \n")
                    valida_campo = verifica_campo_string("nome", novo_nome)
                    if valida_campo == True:
                        novo_nome = novo_nome.lower()
                        break

                #NOVO PREÇO
                valida_campo = False
                while True:
                    novo_preco = input("Digite o novo preço do produto: \n")
                    valida_campo = verifica_campo_float(novo_preco)
                    if valida_campo == True:
                        break

                #NOVA CATEGORIA
                listar_categorias()
                valida_campo = False
                while True:
                    nova_categoria = input("Digite a nova categoria do produto: \n")
                    valida_campo = verifica_campo_string("nome", nova_categoria)
                    if valida_campo == True:
                        nova_categoria = nova_categoria.lower()
                        break

                produtos[produto] = f"{codigoInserido},{novo_nome},{novo_preco},{nova_categoria}"

    # Reescreve o arquivo.txt com a lista com as novas informações!
    with open("produtos.txt", "w") as file:
        for x in produtos:
            file.write(f"{x}\n")

    if contador == 0:
        print("Codigo não localizado!\n")
    else:
        print("Produto alterado com sucesso!\n")


def deletar_produto(codigo):
    produtos = []
    contador = 0
    produtos.clear()

    with open("produtos.txt", "r") as file:

        codigo_inserido = codigo

        for i in file:
            produtos.append(i.strip())
        try:
            for produto in range(len(produtos)):
                cod = produtos[produto].split(",")[0]
                if codigo_inserido == cod:
                    contador = 1

                    produtos.remove(produtos[produto])
        except:
            pass

    with open("produtos.txt", "w") as file:
        for x in produtos:
            file.write(f"{x}\n")

    if contador == 0:
        print("Codigo não localizado!\n")
    else:
        print("Produto deletado com sucesso!\n")


# ------------Funções Categoria---------------------------


def cadastrar_categoria(nome: str):
    with open("categorias.txt", "a") as file:
        dados = f"{nome}\n"
        file.write(dados)
        print("Categoria cadastrada com sucesso! \n")


def listar_categorias():
    categorias_list.clear()
    print(f"Lista de categorias: \n")
    with open("categorias.txt", "r") as file:
        for i in file:
            print(i.strip())
            categorias_list.append(i.strip())
            print("-----------------")
    print("\n")


def deletar_categoria(nome):
    categorias = []
    contador = 0
    categoria = 0

    categorias.clear()
    produtos_categoria.clear()

    with open("categorias.txt", "r") as file:

        nome_inserido = nome

        for i in file:
            categorias.append(i.strip())

        for index_categoria in range(len(categorias)):
            if nome_inserido == categorias[index_categoria]:
                contador = 1
                categorias.remove(categorias[index_categoria])
                break

    if contador == 0:
        print("Codigo não localizado!\n")
    else:
        print("Categoria deletado com sucesso!\n")

        with open("categorias.txt", "w") as file:
            for x in categorias:
                file.write(f"{x}\n")

        with open("produtos.txt", "r") as file:
            for produtos_arquivo in file:
                produtos_categoria.append(produtos_arquivo.strip())

        print("Produtos da categoria alterados:\n")
        for prod in range(len(produtos_categoria)-1):
            try:
                cod_prod = produtos_categoria[prod].split(",")[0]
                prod_nome = produtos_categoria[prod].split(",")[1]
                prod_preco = produtos_categoria[prod].split(",")[2]
                cat_produto = produtos_categoria[prod].split(",")[3]

                if nome == cat_produto:
                    produtos_categoria[prod] = produtos_categoria[prod].replace(nome, "NULL")
                    print(f"{produtos_categoria[prod]}")
            except:
                pass
        print(f"-----------------------------\n")

        with open("produtos.txt", "w") as file:
            for prod in produtos_categoria:
                file.write(f"{prod}\n")


# ------------Funções Venda---------------------------

def informar_cliente():
    login_cliente = input("Deseja logar como cliente?\n"
                          "Informe seu CPF:\n")

    login = verifica_cpf_login(login_cliente)

    if login == True:
        print(f"Cliente logado: {login_cliente}")
        return login_cliente
    else:
        print("Cpf nao localizado!")
        return False


def carrinho_adicionar():
    cod = ""
    listar_produtos()
    while True:
        carrinho_compras.append(input("Digite o codigo do produto desejado.\n"))
        cod = input("Deseja adicionar mais algum produto? Digite S, ou qualquer outro character para sair.\n")
        if cod == "S":
            pass
        else:
            break


def carrinho_remover():
    produtos_no_carrinho.clear()
    cod = ""
    print("PRODUTOS NO CARRINHO: ")

    with open("produtos.txt", "r") as file:
        for produtos_arquivo in file:
            produtos_no_carrinho.append(produtos_arquivo.strip())

    for item in carrinho_compras:
        for prod in range(len(produtos_no_carrinho)):
            try:
                cod_prod = produtos_no_carrinho[prod].split(",")[0]
                prod_nome = produtos_no_carrinho[prod].split(",")[1]
                prod_preco = produtos_no_carrinho[prod].split(",")[2]
                cat_produto = produtos_no_carrinho[prod].split(",")[3]

                if item == cod_prod:
                    print(f"{produtos_no_carrinho[prod]}")
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
            elif item_a_remover in carrinho_compras:
                valida_campo = verifica_campo_numerico(item_a_remover)
                carrinho_compras.remove(item_a_remover)
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
    listar_categorias()
    cat = input("Informe a categoria: \n")

    print(f"Lista de categorias:\n")

    with open("produtos.txt", "r") as file:
        for produtos_arquivo in file:
            produtos_categoria.append(produtos_arquivo.strip())

    try:
        for prod in range(len(produtos_categoria)):
            cat_produto = produtos_categoria[prod].split(",")[3]
            if cat == cat_produto:
                print(produtos_categoria[prod])
    except:
        pass

    return produtos_categoria


def finalizar_carrinho():
    car_products = ""
    pre_produto = float("0.00")
    pre = 0
    npdt = ""
    vpdt = 0
    valor_compra = 0

    produtos_no_carrinho.clear()

    if len(carrinho_compras) > 0:
        with open("produtos.txt", "r") as file:
            for produto in file:
                produtos_no_carrinho.append(produto.strip())

        print(f"ITEM    |   PRECO")
        try:
            for codigos in carrinho_compras:
                for prod in range(len(produtos_no_carrinho)):
                    cpdt = produtos_no_carrinho[prod].split(",")[0]
                    if codigos == cpdt:
                        pre_produto = float(pre_produto) + float(produtos_no_carrinho[prod].split(",")[2])
                        npdt = produtos_no_carrinho[prod].split(",")[1]
                        vpdt = float(produtos_no_carrinho[prod].split(",")[2])
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
                valida_campo = verifica_campo_float(dinheiro_recebido)
                if valida_campo == True:
                    dinheiro_recebido = float(dinheiro_recebido)
                    break

            if dinheiro_recebido >= valor_total:
                print(f"Troco: R${dinheiro_recebido - valor_total}\n")

                data_atual = datetime.now()
                data_atual = data_atual.strftime("%Y-%m-%d")

                hora_agora = datetime.now()
                hora_agora = hora_agora.strftime("%Y-%m-%d %H:%M:%S")

                for codigos in carrinho_compras:
                    car_products = f"{car_products}{codigos};"

                with open("vendas.txt", "a") as file:
                    file.write(f"{hora_agora},{valor_total},{car_products}\n")
                print(f"Compra efetuada: {hora_agora},{valor_total},{car_products}")

                carrinho_compras.clear()
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
                valida_campo = verifica_campo_numerico(card)
                if valida_campo == True:
                    break

            while True:
                senha = input("Insira sua senha:\n")
                valida_campo = verifica_campo_numerico(senha)
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

                        for codigos in carrinho_compras:
                            car_products = f"{car_products}{codigos};"

                        with open("vendas.txt", "a") as file:
                            file.write(f"{hora_agora},{valor_total},{car_products}\n")
                        print(f"Compra efetuada: {hora_agora},{valor_total},{car_products}")

                        with open("credit_cards.txt", "w") as file:
                            cartoes.remove(f"{card},{senha},{cartao_validade},{saldo_total}")
                            cartoes.append(f"{card},{senha},{cartao_validade},{novo_saldo_cartao}")
                            for t in cartoes:
                                file.write(f"{t}\n")

                        carrinho_compras.clear()
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


# Menu-----------------------------------------------------------------
while True:
    print("1-Area do Cliente")
    print("2-Area do Produto")
    print("3- Consultas")
    print("4-Sair")

    menu_geral = input("Digite a opção desejada:\n")

    if menu_geral in menu_geral_validos:
        if int(menu_geral) == 1:
            while True:
                print("1. Nova Venda\n"
                      "2. Cadastrar cliente\n"
                      "3. Voltar\n")

                menu_cliente = input("Digite a opção desejada:\n")

                if menu_cliente in menu_cliente_validos:
                    if int(menu_cliente) == 1:
                        while True:
                            print("1. Informar cliente:\n"
                                  "2. Adicionar produto:\n"
                                  "3. Remover produto:\n"
                                  "4. Listar categorias dos produtos:\n"
                                  "5. Listar produtos de categoria:\n"
                                  "6. Finalizar compras\n"
                                  "7. Voltar\n")

                            menu_cliente_carrinho = input("Digite a opção desejada:\n")
                            if menu_cliente_carrinho in menu_cliente_carrinho_validos:
                                if int(menu_cliente_carrinho) == 1:
                                    informar_cliente()

                                elif int(menu_cliente_carrinho) == 2:
                                    carrinho_adicionar()

                                elif int(menu_cliente_carrinho) == 3:
                                    carrinho_remover()

                                elif int(menu_cliente_carrinho) == 4:
                                    listar_categorias()

                                elif int(menu_cliente_carrinho) == 5:
                                    listar_produtos_categoria()

                                elif int(menu_cliente_carrinho) == 6:
                                    finalizar_carrinho()

                                elif int(menu_cliente_carrinho) == 7:
                                    break
                            else:
                                print("Digite um valor valido do menu!")
                                pass

                    elif int(menu_cliente) == 2:
                        menu_cliente_cpf = input("Digite seu cpf:\n")

                        menu_cliente_cpf = menu_cliente_cpf.replace('.', '').replace('-', '')

                        valida_cpf = verifica_cliente(menu_cliente_cpf)

                        if valida_cpf == True:
                            #NOME
                            valida_campo = False
                            while True:
                                menu_cliente_nome = input("Digite seu nome:\n")
                                valida_campo = verifica_campo_string("nome", menu_cliente_nome)
                                if valida_campo == True:
                                    menu_cliente_nome = menu_cliente_nome.lower()
                                    break

                            #IDADE
                            valida_campo = False
                            while True:
                                menu_cliente_idade = input("Digite seu idade:\n")
                                valida_campo = verifica_campo_numerico(menu_cliente_idade)
                                if valida_campo == True:
                                    break

                            cadastrar_cliente(menu_cliente_cpf, menu_cliente_nome, menu_cliente_idade)

                    elif int(menu_cliente) == 3:
                        break
                else:
                    print("Digite um valor valido do menu!")
                    pass

        if int(menu_geral) == 2:
            while True:
                print("1. Cadastrar produto:\n"
                      "2. Cadastrar categoria:\n"
                      "3. Alterar produto:\n"
                      "4. Listar produtos:\n"
                      "5. Listar categorias:\n"
                      "6. Deletar produto:\n"
                      "7. Deletar categoria:\n"
                      "8. Voltar:\n")

                menu_produto = input("Digite a opção desejada: ")

                if menu_produto in menu_produto_validos:
                    if int(menu_produto) == 1:

                        #CODIGO PRODUTO
                        valida_campo = False
                        while True:
                            menu_produto_codigo = input("Digite o codigo do produto:\n")
                            valida_campo = verifica_campo_numerico(menu_produto_codigo)
                            if valida_campo == True:
                                break

                        #NOME PRODUTO
                        valida_campo = False
                        while True:
                            menu_produto_nome = input("Digite o nome do produto:\n")
                            valida_campo = verifica_campo_string("nome", menu_produto_nome)
                            if valida_campo == True:
                                nome_funcionario = menu_produto_nome.lower()
                                break

                        #PRECO PRODUTO
                        valida_campo = False
                        while True:
                            menu_produto_preco = input("Digite o preco do produto:\n")
                            valida_campo = verifica_campo_float(menu_produto_preco)
                            if valida_campo == True:
                                break

                        #NOME CATEGORIA
                        listar_categorias()
                        valida_campo = False
                        while True:
                           menu_produto_categoria = input("Digite a categoria do produto:\n")
                           valida_campo = verifica_campo_string("nome", menu_produto_categoria)
                           if valida_campo == True:
                               menu_produto_categoria = menu_produto_categoria.lower()
                               break

                        cadastrar_produto(menu_produto_codigo, menu_produto_nome, menu_produto_preco,
                                          menu_produto_categoria)

                    elif int(menu_produto) == 2:

                        #NOME CATEGORIA
                        valida_campo = False
                        while True:
                            menu_produto_categoria_nome = input("Digite a categoria:\n")
                            valida_campo = verifica_campo_string("nome", menu_produto_categoria_nome)
                            if valida_campo == True:
                                nome_funcionario = menu_produto_categoria_nome.lower()
                                break

                        cadastrar_categoria(menu_produto_categoria_nome)

                    elif int(menu_produto) == 3:
                        listar_produtos()
                        menu_produto_alterar_codigo = input("Digite o código do produto a ser alterado:\n")
                        alterar_produto(menu_produto_alterar_codigo)

                    elif int(menu_produto) == 4:
                        listar_produtos()

                    elif int(menu_produto) == 5:
                        listar_categorias()

                    elif int(menu_produto) == 6:
                        listar_produtos()
                        menu_produto_deletar = input("Digite um codigo de produto para ser removido:\n")
                        deletar_produto(menu_produto_deletar)

                    elif int(menu_produto) == 7:
                        listar_categorias()

                        #CATEGORIA
                        valida_campo = False
                        while True:
                           menu_produto_categoria_deletar = input("Digite o nome da categoria a ser removida.\n")
                           valida_campo = verifica_campo_string("nome", menu_produto_categoria_deletar)
                           if valida_campo == True:
                               menu_produto_categoria_deletar = menu_produto_categoria_deletar.lower()
                               break

                        deletar_categoria(menu_produto_categoria_deletar)

                    elif int(menu_produto) == 8:
                        break
                else:
                    print("Digite um valor valido do menu!")
                    pass

        if int(menu_geral) == 3:
            while True:
                print("1. Consulta clientes cadastrados:\n"
                      "2. Histórico de vendas:\n"
                      "3. Voltar:\n")

                menu_consulta = input("Digite a opção desejada:\n")  # Escolha da opcao

                if menu_consulta in menu_consulta_validos:
                    if int(menu_consulta) == 1:
                        listar_clientes()

                    elif int(menu_consulta) == 2:
                        listar_vendas()

                    elif int(menu_consulta) == 3:
                        break
                else:
                    print("Digite um valor valido do menu!")
                    pass

        if int(menu_geral) == 4:
            break
    else:
        print("Digite um valor valido do menu!")
        pass