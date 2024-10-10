sexo = str(input('Digite seu sexo: [M/F:] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos.Digite novamente o seu sexo: ')).upper().strip()[0]
print('Sexo {} armazenado com sucesso! '.format(sexo))

