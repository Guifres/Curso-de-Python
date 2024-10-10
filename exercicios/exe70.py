print('-' *20)
print('  lojas do guifres'.upper())
print('-' * 20)
total = abaixo1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Digite o valor do produto: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        abaixo1000 += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar comprar S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('resumo das suas compras'.upper()))
print(f'O total da compra foi R${total:.2f}')
print(f'temos {abaixo1000} produtos que custa mais R$1000')
print(f'O produto mais barato foi {produto} que custou R${menor:.2f} ')