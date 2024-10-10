from random import randint
from time import sleep
def sorteando(* num):
    cont = 0
    while True:
        s = randint(num[0], num[1])
        cont += 1
        numeros.append(s)
        if cont >= 5:
            break
    print('Sorteando 5 valores da lista: ', end='')
    for i, c in enumerate(numeros):
        print(f'{c}', end=' ')
        sleep(0.5)
def somapar(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f'\nSomando os valores pares de {numeros}, temos {total} ')


numeros = []
sorteando(1, 10)
somapar(numeros)