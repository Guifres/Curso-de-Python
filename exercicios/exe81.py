numeros = []
numeros.append(int(input('Digite um numero: ')))
num = 1
while True:
        resposta = str(input('Quer continuar: S/N ')).strip().upper()[0]
        if resposta == 'S':
            numeros.append(int(input('Digite um numero: ')))
            num += 1

        else:
            break
print(f'Voçê digitou {num} valores')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente é: {numeros}')
if 5 in numeros:
    print(f'O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')
