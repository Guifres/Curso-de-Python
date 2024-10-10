import moedas
num = float(input('digite um numero: R$'))
print(f'A metade de {moedas.moedas(num)} é igual {moedas.moedas(moedas.metade(num))}')
print(f'O dobro de {moedas.moedas(num)} é igual {moedas.moedas(moedas.dobro(num))}')
print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumentar(num))}')
print(f'Diminuindo 13%, temos {moedas.moedas(moedas.diminuir(num))}')
