while True:
    num = int(input('Digite um numero para saber sua tabuada: '))
    if num < 0:
            break
    print('-' * 20)
    for c in range(1, 11):
        r = num * c
        print(f'{c} X {num} = {r} ')
    print('-' * 20)
print('Programa tabuada encerrado. volte sempre'.upper())
