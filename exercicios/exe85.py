numeros = [[], []]
valor = 0
for c in range(0, 7):
    valor = (int(input('Digite um valor: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
print(f'OS valores pares são {numeros[0]}')
numeros[1].sort()
print(f'OS numeros impares são {numeros[1]}')