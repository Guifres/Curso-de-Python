'''c = 1
while c < 10:
    print(c)
    c += 1
print( 'fim'.upper())'''

'''n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('fim'.upper())'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? S/N: ')).upper()
print('fim'.upper())'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voçê digitou {} numeros pares e {} numeros impares.'.format(par, impar))

