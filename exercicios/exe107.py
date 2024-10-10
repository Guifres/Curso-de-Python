from modulos import moedas
num = float(input('digite um numero: R$'))
print(f'A metade de {num} é igual {moedas.metade(num)}')
print(f'O dobro de {num} é igual {moedas.dobro(num)}')
print(f'Aumentando 10%, temos {moedas.aumentar(num)}')
print(f'Diminuindo 13%, temos {moedas.diminuir(num)}')
