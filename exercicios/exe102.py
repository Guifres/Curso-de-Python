def fatorial(num, show=True):
    c = num
    f = 1
    if show == True:
        while c > 0:
            print(f'{c}', end=' ')
            print('X' if c > 1 else '=', end=' ')
            f *= c
            c -= 1
        return f
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f

n = int(input('Digite um numero inteiro: '))
sho = str(input('T para verdadeiro. F para falso: ')).upper()[0]
if sho in 'T':
    sho = True
    print(f'{fatorial(n, show=sho)}', end='')
elif sho in 'F':
    sho = False
    print(f'{fatorial(n, show=sho)}', end='')
