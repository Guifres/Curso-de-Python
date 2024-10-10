import moeda
num = float(input('digite um numero: R$'))
print(f'A metade de {num} é igual {moeda.metade(num)}')
print(f'O dobro de {num} é igual {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(num)}')
