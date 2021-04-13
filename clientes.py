import main
import cpf_tools as validator

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


def verifica_cpf_login(cpf: str):
    contador_cpf_validador = 0
    main.lista_cadastrados.clear()

    with open("clientes.txt", "r") as file:
        for i in file:
            main.lista_cadastrados.append(i.strip())

    for cli in range(len(main.lista_cadastrados)):
        cpf_cadastro = main.lista_cadastrados[cli].split(",")[0]
        if cpf == cpf_cadastro:
            contador_cpf_validador = 1

    if int(contador_cpf_validador) == 1:
        return True
    else:
        return False


def verifica_cliente(cpf: str):
    contador_validador = 0
    main.lista_cadastrados.clear()
    with open("clientes.txt", "r") as file:
        for i in file:
            main.lista_cadastrados.append(i.strip())

    for cli in range(len(main.lista_cadastrados)):
        cpf_cadastro = main.lista_cadastrados[cli].split(",")[0]
        if cpf == cpf_cadastro:
            contador_validador = 1

    cpf_valido = main.validator.cpf_str_validation(cpf)

    if cpf_valido == False and int(contador_validador) == 0:
        contador_validador = 2

    if int(contador_validador) == 0:
        return True
    elif int(contador_validador) == 1:
        print("CPF já existe um cadastro desse cpf.\n")
        return False
    elif int(contador_validador) == 2:
        print("CPF inválido\n")
        return False
