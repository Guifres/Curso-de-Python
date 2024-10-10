n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Voce foi \033[;31mREPROVADO.')
elif 5.0 <= m <= 6.9:
    print('Voce esta de \033[;33mRECUPERAÇÃO.')
else:
    print('Parabens voce foi \033[;34mAPROVADO.')
