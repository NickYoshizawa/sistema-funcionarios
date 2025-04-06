# Cria validação de entrada

def input_str(msg: str, none_permission: bool = False):
    while True:
        try:
            x = str(input(msg))
            if x != "" or none_permission:
                break
            else:
                raise Exception("Digite algo válido!")
        except Exception as e:
            print(e)
    return None if x == "" else x


def input_float(msg: str, none_permission: bool = False) -> float:
    while True:
        try:
            x = str(input(msg))
            if x == "" and none_permission:
                break
            x = float(x)
            break
        except:
            print("Valor inválido. Tente Novamente!")
    return None if x == "" else x

def input_int(msg: str, none_permission: bool = False) -> int:
    while True:
        try:
            x = str(input(msg))
            if x == "" and none_permission:
                break
            x = int(x)
            break
        except:
            print("Valor inválido. Tente Novamente!")
    return None if x == "" else x

def input_gmail(msg: str, none_permission: bool = False) -> str:
    while True:
        try:
            x = str(input(msg))
            if x == "" and none_permission:
                break
            if '@gmail.com' not in x:
                raise Exception("Email Google inválido. Tente Novamente!")
            break
        except Exception as e:
            print(e)
    return None if x == "" else x

def input_idade(msg: str, none_permission: bool = False) -> int:
    while True:
        x = input_int(msg, none_permission=none_permission)
        if x == "":
            break
        if x >= 100 or x <= 15:
            print("Idade inválida. Tente Novamente!")
            continue
        break
    return None if x == "" else x

def input_cpf(msg: str, none_permission: bool = False) -> int:
    while True:
        x = input_int(msg, none_permission=none_permission)
        if x == "":
            break
        if len(str(x)) == 11:
            break
        print("CPF inválido. Tente Novamente!")
    return None if x == "" else x 