import moedas
num = float(input('digite um numero: R$'))
print(f'A metade de {moedas.moeda(num)} é igual {moedas.metade(num, True)}')
print(f'O dobro de {moedas.moeda(num)} é igual {moedas.dobro(num, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(num,10, True)}')
print(f'Diminuindo 13%, temos {moedas.diminuir(num, 13, True)}')
