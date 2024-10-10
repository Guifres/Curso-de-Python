c = total = cont = 0
c = int(input('Digite um numero: [ 999 para parar] '))
while c != 999:
    total += c
    cont += 1
    c = int(input('Digite um numero: [ 999 para parar] '))
print('Voçê digitou {} numeros e a soma deles é = {}'.format(cont, total))