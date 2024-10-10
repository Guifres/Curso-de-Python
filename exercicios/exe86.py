matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        valor = (int(input(f'Digite um valor para a posição [{i}]:[{j}]: ')))
        matriz[i].append(valor)
for linha in matriz:
    print(linha)

