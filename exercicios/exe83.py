exp = str(input('Digite uma expressão: '))
pilha = []
for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(simbolo) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é valida ')
else:
    print('A expressão é invalida ')