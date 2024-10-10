print('-=-' * 10)
print('''      Termos de uma pa'''.upper())
print('-=-' * 10)
primeiro = int(input('Digite um numero: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont += 1
    print('pausa'.upper())
    mais = int(input('Quantos termos voçê quer mostrar a mais? '))
print('A quantidade de termos totais e {}'.format(total))

