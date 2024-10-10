print('-=-' * 10)
print('''      Termos de uma pa'''.upper())
print('-=-' * 10)
primeiro = int(input('Digite um numero: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razão
    cont += 1
print(' fim'.upper())

