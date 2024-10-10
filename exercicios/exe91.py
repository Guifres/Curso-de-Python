from random import randint
from time import sleep
from operator import itemgetter
lista = {}
ranking = {}
print('     Valores sorteados'.upper())
lista['jogador 1'] = randint(1, 6)
lista['jogador 2'] = randint(1, 6)
lista['jogador 3']= randint(1, 6)
lista['jogador 4'] = randint(1, 6)
print('='*30)
for k,v in lista.items():
    print(f'O {k} tirou o numero {v}')
    sleep(1)
print('='*30)
print('    ranking de jogadores:'.upper())
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True )
for i,v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)
