from random import randint
lista = list()
jogos  = list()
print('-='* 20)
print('              mega sena'.upper())
print('-='* 20)
quantidade = int(input('Quantos jogos voçê quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('='*10, f'sorteando {quantidade} jogos'.upper(), '='*10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

