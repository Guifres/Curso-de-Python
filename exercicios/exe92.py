from datetime import date
empresa = {}
empresa['trabalhador'] = str(input('Nome: ')).upper()
ano = int(input('Ano de Nascimemto: '))
while True:
    empresa['carteira'] = int(input('Carteira de Trabalho: [0 não tem] '))
    if empresa['carteira'] > 0:
        empresa['contrato'] = int(input('Ano de contratação: '))
        empresa['salario'] = float(input('Salario: R$ '))
        tempo = date.today().year
        empresa['idade'] = tempo - ano
        aposentadoria = tempo - empresa['contrato'] + 30 + empresa['idade']
        print('='*20)
        print(f'Nome tem o valor de {empresa['trabalhador']}')
        print(f'Idade tem valor {empresa['idade']}')
        print(f'ctps tem o valor de {empresa['carteira']}')
        print(f'Ano de contratação {empresa['contrato']}')
        print(f'Salario tem o valor R${empresa['salario']}')
        print(f'Voçê ira se aposentar aos {aposentadoria}')
        break
    else:
        tempo = date.today().year
        empresa['idade'] = tempo - ano
        print('='* 20)
        print(f'Nome tem o valor de {empresa['trabalhador']}')
        print(f'Idade tem valor {empresa['idade']}')
        print(f'ctps tem o valor de {empresa['carteira']}')
        break
print('fim'.upper())

