def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols}')

jogador = str(input('Nome do jogador: '))
gol = str(input('Numero de gols: '))
if gol.isnumeric():
    gol= int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
