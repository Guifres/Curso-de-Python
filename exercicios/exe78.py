valores = []
for cont in range(0, 6):
    valores.append(int(input('Digite um numero: ')))
print(f'Os numeros digitados foram {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for v, i in enumerate(valores):
    if i == max(valores):
        print(f'{v}...', end='')
print(f'\nO menor numero digitado foi {min(valores)} na posição ', end='')
for v, i in enumerate(valores):
    if i == min(valores):
        print(f'{v}...', end='')
