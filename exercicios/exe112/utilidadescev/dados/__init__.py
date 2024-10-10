
def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace('.', ',').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mError. {entrada} e um preço invalido.\033[0;31m ')
        else:
            valido = True
            return float(entrada)
