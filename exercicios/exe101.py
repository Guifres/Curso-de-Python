from datetime import date
def voto(ano):
    global idade
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return f'Com {idade} anos o: Voto obrigatorio!'
    if idade > 18:
        return f'Com {idade} anos : Não vota!'
    if idade >= 65:
        return f'Com {idade} anos o : Voto opcional!'
    print(idade)


ano = int(input('Digite o ano de nascimento: '))
print(f'{voto(ano)}')