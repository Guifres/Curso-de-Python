tot18 = 0
sexm = 0
m20 = 0
while True:
    idade = int(input('Sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu sexo M/F: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        sexm += 1
    if sexo == 'F' and idade <= 20:
        m20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18} ')
print(f'Ao todo temos {sexm} homem cadastrado')
print(f'E temos {m20} mulheres com menos de 20 anos')



