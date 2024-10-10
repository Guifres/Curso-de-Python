galera = []
dados = {}
total = media = 0
while True:
    dados.clear()
    dados['nomes'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro.Digite novamente M ou F...')
    dados['Idade'] = int(input('Idade: '))
    total += dados['Idade']
    galera.append(dados.copy())
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro.Digite novamente S ou N... ')
    if resposta in 'Nn':
        break
print(f'Foram cadastradas {len(galera)} pessoas.´')
media = total / len(galera)
print(f'A media de idade das pessoas é {media}')
print('Mulheres cadastradas ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nomes']}', end='')
print()
print('lista de pessoas acima da media:')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end=' ')
        for k, i in p.items():
            print(f'{k} = {i}: ', end='')
        print()

