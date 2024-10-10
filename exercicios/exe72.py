ex = ('Zero', 'Um','Dois', 'Três', 'Quatro',
      'Cinco', 'Seis', 'Sete ', 'Oito', 'Nove',
      'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
      'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
      'Dezenove', 'Vinte')
resposta = ''
while True:
    numeros = int(input('Digite um numero entre 0 e 20: '))
    if numeros <= 20:
        break
print(f'{numeros} por extenso é: {ex[numeros]}')
