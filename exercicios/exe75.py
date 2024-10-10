numeros = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ' )),
           int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 aparece na {numeros.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado nenhuma vez')
print(f'os numeros pares digitados foram ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
