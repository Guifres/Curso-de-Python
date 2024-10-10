from time import sleep
def maior(* num):
    print('=' * 35)
    print('Analizando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {max(num)}')
    sleep(0.5)


maior(2, 5, 6, 8, 7, 9)
maior(2, 6, 5, 7)
maior(0, 5, 1)
maior(1, 5)
maior(0)