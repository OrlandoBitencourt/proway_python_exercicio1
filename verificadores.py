import string


symbols = ['!', '@', '#', '$', '%', '^', '&',
           '*', '(', ')', '<', '>', ',', '=',
           '´', '`', '¨', '^', "~", "'", '"',
           "'", "ª", "º", "{", "}", "-", "[",
           "]"]

numeros = '0123456789'
alfabeto = string.ascii_letters

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