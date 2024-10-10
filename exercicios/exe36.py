valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
mese = int(input('Quantos anos o financiamento: '))
meses = mese * 12
parcelas = valor / mese
if parcelas <= salario * 30 / 100:
    print('Parabens seu emprestimo foi aprovado, o valor da sua parcela sera R${:.2f}'.format(parcelas))
else:
    print('Seu emprestimo foi negado, pois o valor da parcela ultrapassa 30% do seu salario!'
          '')
