def metade(n=0):
    f = n / 2
    return f

def dobro(n=0):
    f = n * 2
    return f

def aumentar(n=0):
    f = n + (n * 10 / 100)
    return f

def diminuir(n=0):
    f = n - (n * 13 / 100)
    return f

def moedas(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')