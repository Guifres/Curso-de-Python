soma = 0
conte = 0
for c in range(1, 7):
     num = int(input('Digite o {}º valor: '.format(c)))
     if num % 2 == 0:
         soma += num
         conte += 1
print('Voçê informou {} numeros PARES e a soma deles é {}'.format(conte, soma))
