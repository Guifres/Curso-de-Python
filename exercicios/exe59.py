from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior 
[ 4 ] Novos numeros 
[ 5 ] Sair do programa.''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        mul = n1 * n2
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, mul))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o valor maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Digite um valor: '))
        n2 + int(input('Digite outro valor: '))
    elif opção == 5:
        sleep(1)
        print('finalizando'.upper())
    else:
        print('Opção invalida tente novamente.')
    sleep(1)
print('Fim do programa, volte sempre!')
