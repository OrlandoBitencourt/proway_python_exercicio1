from datetime import datetime
import cpf_tools as validator
import string
import clientes
import produtos
import vendas
import categorias
import verificadores


from verificadores import verifica_campo_float, verifica_campo_string, verifica_campo_numerico

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
                                    vendas.informar_cliente()

                                elif int(menu_cliente_carrinho) == 2:
                                    vendas.carrinho_adicionar()

                                elif int(menu_cliente_carrinho) == 3:
                                    vendas.carrinho_remover()

                                elif int(menu_cliente_carrinho) == 4:
                                    categorias.listar_categorias()

                                elif int(menu_cliente_carrinho) == 5:
                                    vendas.listar_produtos_categoria()

                                elif int(menu_cliente_carrinho) == 6:
                                    vendas.finalizar_carrinho()

                                elif int(menu_cliente_carrinho) == 7:
                                    break
                            else:
                                print("Digite um valor valido do menu!")
                                pass

                    elif int(menu_cliente) == 2:
                        menu_cliente_cpf = input("Digite seu cpf:\n")

                        menu_cliente_cpf = menu_cliente_cpf.replace('.', '').replace('-', '')

                        valida_cpf = clientes.verifica_cliente(menu_cliente_cpf)

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

                            clientes.cadastrar_cliente(menu_cliente_cpf, menu_cliente_nome, menu_cliente_idade)

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
                        categorias.listar_categorias()
                        valida_campo = False
                        while True:
                           menu_produto_categoria = input("Digite a categoria do produto:\n")
                           valida_campo = verifica_campo_string("nome", menu_produto_categoria)
                           if valida_campo == True:
                               menu_produto_categoria = menu_produto_categoria.lower()
                               break

                        produtos.cadastrar_produto(menu_produto_codigo, menu_produto_nome, menu_produto_preco,
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

                        categorias.cadastrar_categoria(menu_produto_categoria_nome)

                    elif int(menu_produto) == 3:
                        produtos.listar_produtos()
                        menu_produto_alterar_codigo = input("Digite o código do produto a ser alterado:\n")
                        produtos.alterar_produto(menu_produto_alterar_codigo)

                    elif int(menu_produto) == 4:
                        produtos.listar_produtos()

                    elif int(menu_produto) == 5:
                        categorias.listar_categorias()

                    elif int(menu_produto) == 6:
                        produtos.listar_produtos()
                        menu_produto_deletar = input("Digite um codigo de produto para ser removido:\n")
                        produtos.deletar_produto(menu_produto_deletar)

                    elif int(menu_produto) == 7:
                        categorias.listar_categorias()

                        #CATEGORIA
                        valida_campo = False
                        while True:
                           menu_produto_categoria_deletar = input("Digite o nome da categoria a ser removida.\n")
                           valida_campo = verifica_campo_string("nome", menu_produto_categoria_deletar)
                           if valida_campo == True:
                               menu_produto_categoria_deletar = menu_produto_categoria_deletar.lower()
                               break

                        categorias.deletar_categoria(menu_produto_categoria_deletar)

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
                        clientes.listar_clientes()

                    elif int(menu_consulta) == 2:
                        vendas.listar_vendas()

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