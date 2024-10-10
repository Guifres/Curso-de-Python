num = int(input('Digite um numero inteiro: '))
n = int(input('''Voçe quer converter esse numero para:
[ 1 ] Binario
[ 2 ] Octal
[ 3 ] hexadecimal
Digite o numero da opção: '''))
if n == 1:
    print('Seu numero convertido para BINARIO e: {}'.format(bin(num)[2:]))
elif n == 2:
    print('Seu numero convertido para OCTAL e: {}'.format(oct(num)[2:]))
elif n == 3:
    print('Seu numero convertido para HEXADECIMAL e: {}'.format(hex(num)[2:]))

