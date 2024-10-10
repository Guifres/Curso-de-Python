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

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mError.Por favor digite um numero real valido\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar um numero.\033[m')
            return 0
        else:
            return n



n = leiaint('Digite um inteiro: ')
n1 = leiafloat('Digite um numero real. ')
print(f'Os numero digitados foram {n} e {n1}')
