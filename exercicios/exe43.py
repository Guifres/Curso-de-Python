peso = float(input('Qual seu peso: (Kg) '))
altura = float(input('Qual sua altura: (m) '))
imc = peso / ( altura ** 2 )
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO. ')
elif 18.5 <= imc < 25:
    print('Seu peso esta IDEAL. ')
elif 25 <= imc < 30:
    print('SOBREPESO.')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBITA')
