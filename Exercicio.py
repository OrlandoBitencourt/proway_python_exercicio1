from datetime import datetime

clientesList = []
carrinho_compras = []
produtos_categoria = []
produtos_no_carrinho = []

valor_total = 0
#------------Funções Clientes---------------------------

def cadastrar_cliente(cpf: str, nome: str, idade: str):
    with open("clientes.txt", "a") as file:
        dados = f"{cpf},{nome},{idade}\n"
        file.write(dados)


def listar_clientes():
    print(f"Lista de clientes: \n")
    with open("clientes.txt", "r") as file:
        for i in file:
            print(i.strip())
            print("-----------------")

#------------Funções Produtos---------------------------

def cadastrar_produto(codigo: str, nome: str, preco: str, categoria: str):
    with open("produtos.txt", "a") as file:
        dados = f"{codigo},{nome},{preco},{categoria}\n"
        file.write(dados)



def listar_produtos():
    print(f"Lista de produtos: \n")
    with open("produtos.txt", "r") as file:
        for i in file:
            print(i.strip())
            print("-----------------")


def alterar_produto(codigo):
    produtos = []
    contador = 0

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
                novo_nome = input("Digite o novo nome do produto: \n")
                novo_preco = input("Digite o novo preço do produto: \n")
                nova_categoria = input("Digite a nova categoria do produto: \n")

                if novo_nome == "":
                    novo_nome = produtos[produto].split(",")[1]
                if novo_preco == "":
                    novo_preco = produtos[produto].split(",")[2]
                if nova_categoria == "":
                    nova_categoria = produtos[produto].split(",")[3]

                produtos[produto] = f"{codigoInserido},{novo_nome},{novo_preco},{nova_categoria}\n"

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
    with open("produtos.txt", "r") as file:

        codigo_inserido = codigo

        # Puxa informações do file.txt e da append na list
        for i in file:
            produtos.append(i.strip())

        # Busca o produto pelo codigo, e pede informações para serem alteradas
        for produto in range(len(produtos)):
            cod = produtos[produto].split(",")[0]
            if codigo_inserido == cod:
                contador = 1

                produtos.remove(produtos[produto])

    with open("produtos.txt", "w") as file:
        for x in produtos:
            file.write(f"{x}\n")

    if contador == 0:
        print("Codigo não localizado!\n")
    else:
        print("Produto deletado com sucesso!\n")


#------------Funções Categoria---------------------------


def cadastrar_categoria(nome: str):
    with open("categorias.txt", "a") as file:
        dados = f"{nome}\n"
        file.write(dados)

def listar_categorias():
    print(f"Lista de categorias: \n")
    with open("categorias.txt", "r") as file:
        for i in file:
            print(i.strip())
            print("-----------------")


def deletar_categoria(nome):
    categorias = []
    contador = 0
    categoria = 0

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

        for prod in range(len(produtos_categoria)):
            cod_prod = produtos_categoria[prod].split(",")[0]
            prod_nome = produtos_categoria[prod].split(",")[1]
            prod_preco = produtos_categoria[prod].split(",")[2]
            cat_produto = produtos_categoria[prod].split(",")[3]

            if nome == cat_produto:
                print(produtos_categoria[prod])
                produtos_categoria[prod] = produtos_categoria[prod].replace(nome, "NULL")

        with open("produtos.txt", "w") as file:
            for prod in produtos_categoria:
                file.write(f"{prod}\n")

#------------Funções Venda---------------------------

def informar_cliente():
    login_cliente = input("Deseja logar como cliente?\n"
                          "Informe seu CPF:\n")
    return login_cliente


def carrinho_adicionar():
    cod = ""
    listar_produtos()
    while True:
        carrinho_compras.append(input("Digite o codigo do produto desejado.\n"))
        cod = input("Deseja adicionar mais algum produto? S ou N\n")
        if cod == "S":
            pass
        else:
            break



def carrinho_remover():
    cod = ""
    for item in carrinho_compras:
        print(item)

    while True:
        cod = input("Deseja cancelar algum produto? S ou N\n")
        if cod == "S":
            carrinho_compras.remove(input("Digite o codigo do produto a ser cancelado:\n"))
        else:
            break


def listar_produtos_categoria():

    listar_categorias()
    cat = input("Informe a categoria que desejar")

    print(f"Lista de categorias:\n")
    with open("produtos.txt", "r") as file:
        for produtos_arquivo in file:
            produtos_categoria.append(produtos_arquivo.strip())

    for prod in range(len(produtos_categoria)):
        cat_produto = produtos_categoria[prod].split(",")[3]
        if cat == cat_produto:
            print(produtos_categoria[prod])
            
    return produtos_categoria


def finalizar_carrinho():
    car_products = ""
    pre_produto = float("0.00")
    pre = 0
    npdt = ""
    vpdt = 0
    valor_compra = 0
    if len(carrinho_compras) > 0:
        produtos_no_carrinho.clear()
        with open("produtos.txt", "r") as file:
            for produto in file:
                produtos_no_carrinho.append(produto.strip())

        print(f"ITEM    |   PRECO")
        for prod in range(len(produtos_no_carrinho)):
            cpdt = produtos_no_carrinho[prod].split(",")[0]
            if cpdt in carrinho_compras:
                pre_produto = float(pre_produto)+float(produtos_no_carrinho[prod].split(",")[2])
                npdt = produtos_no_carrinho[prod].split(",")[1]
                vpdt = float(produtos_no_carrinho[prod].split(",")[2])
                print(f"{npdt}    |    R${vpdt}")
        valor_total = pre_produto
        print(f"\nValor total da compra: R${str(valor_total)}\n")

        modalidade_pagamento = int(input("Insira a modalidade de pagamento:\n"
                                 "1. Dinheiro\n"
                                 "2. Cartão\n"
                                 "3. Voltar\n"))


        if modalidade_pagamento == 1:
            dinheiro_recebido = float(input("Informe a quantia paga pelo cliente: \n"))
            if dinheiro_recebido >= valor_total:
                print(f"Troco: R${dinheiro_recebido - valor_total}\n")

                hora_agora = datetime.now()

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

            card = input("Insira o numero do cartão:\n")
            senha = input("Insira sua senha:\n")

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

            hora_agora = datetime.now()

            data_atual = datetime.now()
            format = "%Y-%m-%d"
            data_atual = data_atual.strftime(format)

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




#-----------------------------------------------------------------
while True:
    print("1-Area do Cliente")
    print("2-Area do Produto")
    print("3- Consultas")
    print("4-Sair")

    menu_geral = int(input("Digite a opção desejada:\n"))#Escolha da opcao

    if menu_geral == 1:
        while True:
            print("1. Nova Venda\n"
                  "2. Cadastrar cliente\n"
                  "3. Voltar\n")
            menu_cliente = int(input("Digite a opção desejada:\n"))#Escolha da opcao
            if menu_cliente == 1:
                while True:
                    print("1. Informar cliente:\n"
                          "2. Adicionar produto:\n"
                          "3. Remover produto:\n"
                          "4. Listar categorias dos produtos:\n"
                          "5. Listar produtos de categoria:\n"
                          "6. Finalizar compras\n"
                          "7. Voltar\n")
                    menu_cliente_carrinho = int(input("Digite a opção desejada:\n"))

                    if menu_cliente_carrinho == 1:
                        informar_cliente()
                    elif menu_cliente_carrinho == 2:
                        carrinho_adicionar()
                    elif menu_cliente_carrinho == 3:
                        carrinho_remover()
                    elif menu_cliente_carrinho == 4:
                        listar_categorias()
                    elif menu_cliente_carrinho == 5:
                        listar_produtos_categoria()
                    elif menu_cliente_carrinho == 6:
                        finalizar_carrinho()
                    elif menu_cliente_carrinho == 7:
                        break

            elif menu_cliente == 2:
                menu_cliente_nome = input("Digite seu nome:\n")
                menu_cliente_cpf = input("Digite seu cpf:\n")
                menu_cliente_idade = input("Digite seu idade:\n")

                cadastrar_cliente(menu_cliente_cpf, menu_cliente_nome, menu_cliente_idade)
            elif menu_cliente == 3:
                break
    if menu_geral == 2:
        while True:
            print("1. Cadastrar produto:\n"
                  "2. Cadastrar categoria:\n"
                  "3. Alterar produto:\n"
                  "4. Listar produtos:\n"
                  "5. Listar categorias:\n"
                  "6. Deletar produto:\n"
                  "7. Deletar categoria:\n"
                  "8. Voltar:\n")
            menu_produto = int(input("Digite a opção desejada: "))  # Escolha da opcao
            if menu_produto == 1:
                menu_produto_codigo = input("Digite o codigo do produto:\n")
                menu_produto_nome = input("Digite o nome do produto:\n")
                menu_produto_preco = input("Digite o preco do produto:\n")
                menu_produto_categoria = input("Digite a categoria do produto:\n")

                cadastrar_produto(menu_produto_codigo, menu_produto_nome, menu_produto_preco, menu_produto_categoria)

            elif menu_produto == 2:
                menu_produto_categoria_nome = input("Digite a categoria:\n")
                cadastrar_categoria(menu_produto_categoria_nome)
            elif menu_produto == 3:
                menu_produto_alterar_codigo = input("Digite o código do produto a ser alterado:\n")
                alterar_produto(menu_produto_alterar_codigo)
            elif menu_produto == 4:
                listar_produtos()
            elif menu_produto == 5:
                listar_categorias()
            elif menu_produto == 6:
                menu_produto_deletar = input("Digite um codigo de produto para ser removido:\n")
                deletar_produto(menu_produto_deletar)
            elif menu_produto == 7:
                menu_produto_categoria_deletar = input("Digite o nome da categoria a ser removida.\n")
                deletar_categoria(menu_produto_categoria_deletar)
            elif menu_produto == 8:
                break
    if menu_geral == 3:
        while True:
            print("1. Consulta clientes cadastrados:\n"
                  "2. Histórico de vendas:\n"
                  "3. Voltar:\n")
            menu_consulta = int(input("Digite a opção desejada:\n"))  # Escolha da opcao

            if menu_consulta == 1:
                listar_clientes()
            elif menu_consulta == 2:
                listar_vendas()
            elif menu_consulta == 3:
                break
    if menu_geral == 4:
        break