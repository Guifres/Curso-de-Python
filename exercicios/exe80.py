valores = []
for c in range(0, 5):
    n = (int(input('Digite um numero: ')))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado a posição {pos}')
                break
            pos += 1
print(f'Os numeros digitados foram {valores}')