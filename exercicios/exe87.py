matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
par =coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para adicionar a posição: [{l}]:[{c}] '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma de todos os valores pares é {par}')
for l in range(0, 3):
    coluna3 += matriz[l][2]
print(f'A soma de todos os valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


