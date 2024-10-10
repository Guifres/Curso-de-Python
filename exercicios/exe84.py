lista = []
dado = []
maior = maior = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resposta = str(input('Quer continuar [S/N]:  ')).strip().upper()[0]
    if resposta in 'N':
        break
print(f'Ao todo voçê cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi {maior}. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}, '.upper(), end='')
print(f'\nO menor peso foi {menor}. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}, '.upper(), end='')
print()