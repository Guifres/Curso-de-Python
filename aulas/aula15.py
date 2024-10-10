num = s = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    s += num
print(f'A soma foi {s} ')