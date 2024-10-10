from datetime import date
ano = int(input('Qual ano voce nasceu: '))
sexo = str(input('''Qual sexo?
[ 1 ] MASCULINO
[ 2 ] FEMININO: 
Digite a opcção: '''))
atual = date.today().year - ano
if atual < 16 and sexo == '1':
    print('Voce ainda deve se alistar, falta {} anos ainda ate completar o prazo!'.format(16 - atual))
elif atual == 16 and sexo == '1':
    print('Esta na hora de se alistar')
elif sexo == '2' and 1 <= atual <= 100 :
    print('Voçê não precisa se alistar!')
else:
    print('Voce ja passou do prazo de alistamento {} anos.'.format(atual - 16))
