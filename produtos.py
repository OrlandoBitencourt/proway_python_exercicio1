import main
import categorias

def cadastrar_produto(codigo: str, nome: str, preco: str, categoria: str):
    main.produtos_list.clear()
    main.categorias_list.clear()
    temp_prod_codigo = []

    with open("produtos.txt", "r") as file:
        for i in file:
            main.produtos_list.append(i.strip())

    for prod in range(len(main.produtos_list)):
        p = main.produtos_list[prod].split(",")[0]
        temp_prod_codigo.append(p)

    if codigo not in temp_prod_codigo:

        with open("categorias.txt", "r") as file:
            for i in file:
                main.categorias_list.append(i.strip())

        if categoria in main.categorias_list:
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
    main.produtos_list.clear()
    print(f"Lista de produtos: \n")
    with open("produtos.txt", "r") as file:
        for i in file:
            print(i.strip())
            main.produtos_list.append(i.strip())
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
                    valida_campo = main.verifica_campo_string("nome", novo_nome)
                    if valida_campo == True:
                        novo_nome = novo_nome.lower()
                        break

                #NOVO PREÇO
                valida_campo = False
                while True:
                    novo_preco = input("Digite o novo preço do produto: \n")
                    valida_campo = main.verifica_campo_float(novo_preco)
                    if valida_campo == True:
                        break

                #NOVA CATEGORIA
                categorias.listar_categorias()
                valida_campo = False
                while True:
                    nova_categoria = input("Digite a nova categoria do produto: \n")
                    valida_campo = main.verifica_campo_string("nome", nova_categoria)
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
