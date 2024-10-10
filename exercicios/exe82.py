lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resposta = str(input('Quer continuar? S/N')).strip().upper()[0]
    if resposta in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de valores pares digitados: {par}')
print(f'A lista de valores impares digitados: {impar}')