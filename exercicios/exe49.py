from time import sleep
num = int(input('Digite o numero que voçê deseja ver a taboada: '))
print('ESTOU CALCULANDO...')
sleep(1)
for c in range(1, 11):
     print('{} X {} = {}'.format(num, c, num * c))
