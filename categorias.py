import main

def cadastrar_categoria(nome: str):
    with open("categorias.txt", "a") as file:
        dados = f"{nome}\n"
        file.write(dados)
        print("Categoria cadastrada com sucesso! \n")


def listar_categorias():
    main.categorias_list.clear()
    print(f"Lista de categorias: \n")
    with open("categorias.txt", "r") as file:
        for i in file:
            print(i.strip())
            main.categorias_list.append(i.strip())
            print("-----------------")
    print("\n")


def deletar_categoria(nome):
    categorias = []
    contador = 0
    categoria = 0

    categorias.clear()
    main.produtos_categoria.clear()

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
                main.produtos_categoria.append(produtos_arquivo.strip())

        print("Produtos da categoria alterados:\n")
        for prod in range(len(main.produtos_categoria)-1):
            try:
                cod_prod = main.produtos_categoria[prod].split(",")[0]
                prod_nome = main.produtos_categoria[prod].split(",")[1]
                prod_preco = main.produtos_categoria[prod].split(",")[2]
                cat_produto = main.produtos_categoria[prod].split(",")[3]

                if nome == cat_produto:
                    main.produtos_categoria[prod] = main.produtos_categoria[prod].replace(nome, "NULL")
                    print(f"{main.produtos_categoria[prod]}")
            except:
                pass
        print(f"-----------------------------\n")

        with open("produtos.txt", "w") as file:
            for prod in main.produtos_categoria:
                file.write(f"{prod}\n")