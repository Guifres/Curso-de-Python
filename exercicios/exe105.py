
def notas(*n, sit=False):
    '''
    -> Função para analisar notas e medias de alunos
    :param n: uma ou mais notas de alunos ( varias notas)
    :param sit:
    :return:
    '''
    r = {}
    r['notas'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


respo = notas(10, 2.5, 3.2, 5,)
print(respo)