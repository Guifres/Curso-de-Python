s = cont = 0
while True:
    num = int(input('Digite um numero: [ ou 999 para parar]: '))
    if num == 999:
        break
    s += num
    cont += 1
print(f'Voçê digitou {cont} numeros e a soma dos valores digitados foi {s}')
