dados = {}
dados['nome'] = str(input('Nome: ' ))
dados ['media'] = float(input('Media do Aluno: '))
print(f'Nome igual a {dados["nome"]}')
print(f'Media é igual {dados["media"]}')
if dados["media"] <= 4.9:
    print('Sua media foi abaixo de 5, por isso foi REPROVADO...' )
elif dados["media"] <= 6.9:
    print('Voçê esta de RECUPERAÇÃO...')
elif dados["media"] >= 7:
    print('Parabéns voçê foi APROVADO...')
