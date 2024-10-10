from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada: '))
print('\033[;31mJO')
sleep(1)
print('\033[;32mKEN')
sleep(1)
print('\033[;33mPO')
sleep(1)
print('\033[;m-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
     print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU ')
    elif jogador == 2:
        print('COMPUTADOR GANHOU ')
    else:
        print('Opção invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU ')
    elif jogador == 1:
        print('EMPATE ')
    elif jogador == 2:
        print('JOGADOR GANHOU ')
    else:
        print('Opção invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU ')
    elif jogador == 1:
        print('COMPUTADOR GANHOU ')
    elif jogador == 2:
        print('EMPATE ')
    else:
        print('Opção invalida')

