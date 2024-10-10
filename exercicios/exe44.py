print('{:=^40}'.format('LOJAS GUIFRES'))
preço = float(input('Digite o valor da sua compra:R$'))
opção = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] A vista dinheiro ou cheque: 10 % de desconto.
[ 2 ] A vista no cartão: 5% de desconto.
[ 3 ] Em ate 2X no cartão: preço normal.
[ 4 ] 3X ou mais no cartão: 20% de juros.
Digite a opção de pagamento:'''))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada de 2X de R${}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}X de R${:.2f}'.format(totparc, parcela))
else:
    total = preço
    print('\033[;31mOPÇÃO INVALIDA PAGAMENTO. tente novamente!')
print('Sua compra de R${} vai custar R${} no final'.format(preço, total))
