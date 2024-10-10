from time import sleep
def contador(i, m, f ):
    print('='* 30)
    print(f'Contagem de {i} ate {m} de {f} em {f}')
    sleep(1.5)
    for c in range(i, m, f):
        print(f'{c}', end=' ')
        sleep(0.5)
    print()


contador(1,11, 1)
contador(10, 0, -2)
print('='* 30)
print('Agora é dua vez de personalizar a contagem... ')
ini = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if ini > f:
    p = -p
if p == 0:
    p = 1
contador(ini, f, p)
