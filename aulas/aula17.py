'''lista = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10,]
lista [5] = 8
lista.append(11)
lista.sort()
print(lista)
print(f'Essa lista tem {len(lista)} elementos.')'''


'''valores = []
valores.append(11)
valores.append(15)
valores.append(88)
valores.sort()
for pos, c in enumerate(valores):
    print(f'O valor {c} esta na posição {pos}')'''


valores = []
for cont in range(0, 2):
    valores.append(int(input('Digite um numero: ')))
for pos, c in enumerate(valores):
    print(f'O numero {c} esta na posição {pos}')
print('acabou'.upper())