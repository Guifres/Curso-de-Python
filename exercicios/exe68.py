from random import randint
vitoria = 0
print('Vamos jogar Para ou Impar?')
while True:
    jogador = int(input('Digite um numero:'))
    computador = randint(0 ,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Voçê escolhe par ou impar? [P/I]: ')).upper().strip()[0]
    print(f'Jogador jogou {jogador} e computador joogu {computador}, total foi {total}')
    print('Deu par'.upper() if total % 2 == 0 else 'deu impar'.upper())
    if tipo == 'P':
        if total % 2 == 0:
            print('Voçê venceu ')
            vitoria += 1
        else:
            print('Voçê perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voçê venceu')
            vitoria += 1
        else:
            print('Voçê perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over.Voçê venceu {vitoria} vezes')
