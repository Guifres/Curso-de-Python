valores = []
while True:
    n =(int(input('Digite um numero: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor ja existente na lista...')
    resposta = str(input('Quer continuar adicionando valores? S/N ')).strip().upper()[0]
    if resposta == 'N':
        break
valores.sort()
print(f'Os valores digitados foram {valores}')

