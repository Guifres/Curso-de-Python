lanche = 'pizza', 'coxinha', 'enroladinho', 'doce'
for comida in lanche:
    print(f'Eu vou comer {comida}')


for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont} na posição {pos}')


for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont} ')