c = 'S'
cont = total = media = maior = menor = 0
while c in 'Ss':
    num = int(input('Digite um numero: '))
    total += num
    cont += 1
    if cont == 1:
       num = maior = menor
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    c = str(input('Quer continuar? S/N' )).upper().strip()[0]
media = total / cont
print('Voçê digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))