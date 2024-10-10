time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input('Quantas partida ele jogou: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('opção invalida.Responda S ou N...')
    time.append(jogador.copy())
    if resposta in 'Nn':
        break
print(time)
print(f'{"cod":<4}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, p in enumerate(time):
    print(f'{i:<4}', end='')
    for d in p.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('\nQuer mostrar os dados de qual jogador: [999 para paar} '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o codigo {busca}')
    else:
        print(f'-----Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols ')
print('FIM...')