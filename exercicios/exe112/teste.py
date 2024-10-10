from exe112.utilidadescev import moeda
from exe112.utilidadescev import dados

num = dados.leiadinheiro('digite o preço: R$')
p1 = int(input('Quantos % voçê quer aumentar:  '))
p2 = int(input('Quantos % voçê quer diminuir: '))
moeda.resumo(num,p1,p2)
