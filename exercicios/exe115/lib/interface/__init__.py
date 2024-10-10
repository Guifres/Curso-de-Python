def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mError.Por favor digite um numero inteiro valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar o numero.\033[m, ')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[33m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Digite sua opção: ')
    return opc

