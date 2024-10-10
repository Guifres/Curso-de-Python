def metade(n=0, formatado=False):
    f = n / 2
    return f if not formatado else moeda(f)

def dobro(n=0, formatado=False):
    f = n * 2
    return f if not formatado else moeda(f)

def aumentar(n=0, taxa=0, formatado=False):
    f = n + (n * 10 / 100)
    return f if formatado is False else moeda(f)

def diminuir(n=0, taxa=0, formatado=False):
    f = n - (n * 13 / 100)
    return f if formatado is False else moeda(f)

def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')

def resumo(p=0, aumen=10, dimi=5):
    print('-'* 40)
    print(f'Resuno do Valor'.center(40))
    print('-'* 40 )
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'O dobrodo preço: \t{dobro(p, True)}')
    print(f'{aumen}% de aumento: \t{aumentar(p, aumen, True)}')
    print(f'{dimi}% de redução: \t{diminuir(p, dimi, True)}')
