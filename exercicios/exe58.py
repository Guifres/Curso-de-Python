from random import randint
computador = randint(0, 10)
print('Ola pensei em um numero de 0 a 10. Tente adivinhar.')
print('Será que voçê acertou qual foi?')
acertos = False
palpites = 0
while not acertos:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertos = True
    else:
       if jogador < computador:
           print('Mais.tente novamente: ')
       elif jogador > computador:
           print('Menos.tente novamente: ')
print('Acertou com {} tentativas. PARABENS...'.format(palpites))


