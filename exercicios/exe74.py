from random import randint
numeros = (randint(1, 10),randint(1, 10),randint(1, 10),
            randint(1, 10),randint(1, 10))
print(f'Os numeros sorteados foram: ', end=' ' )
for c in numeros:
    print(f'{c}', end=' ')
print(f'\nO menor numero sorteado foi: {min(numeros)}')
print(f'O maior numero sorteado foi: {max(numeros)}')
