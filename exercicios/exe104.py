def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0:31mErro.Digite um numero valido...\33[0:m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'O numero digitado foi {n}')
