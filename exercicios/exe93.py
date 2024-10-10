lista = {}
gols = []
lista['jogador'] = str(input('Jogador: '))
partidas= int(input('Quantas partidas ele jogou? '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
lista['gols'] = gols[:]
lista['total'] = sum(gols)
print('='*30)
print(lista)
print('='*30)
for k, i in lista.items():
    print(f'O campo {k} tem o valor {i} ')
print('='*30)
print(f'O jogador {lista["jogador"].upper()} tem {lista["total"]} gols')
for v, i in enumerate(lista['gols']):
    print(f'Na partida {v}, ele marcou {i} gols ')
