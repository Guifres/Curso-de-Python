lista = []
while True:
    nome = str(input('NOME: ')).upper()
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2 ], media])
    respostas = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if respostas in 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>10} ')
for i, p in enumerate(lista):
    print(f'{i:<4}{p[0]:<11}{p[2]:>8.1f}')
while True:
    opção = int(input('Deseja ver a nota de qual aluno? [999] para parar '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(lista) - 1:
        print(f'As notas de {lista[opção][0]} são {lista[opção][1]}')
print('volte sempre'.upper())