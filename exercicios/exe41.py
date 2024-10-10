from datetime import date
ano = int(input('Digite o ano em que nasceu: '))
atual = date.today().year - ano
print('O atleta tem {} anos.'.format(atual))
if atual <= 9:
    print('Sua catedoria é: \033[;32MIRIM. ')
elif atual <= 14:
    print('Sua categoria é: \033[;33mINFANTIL. ')
elif atual <= 19:
    print('Sua categoria é: \033[;35mJUNIOR. ')
elif atual <= 25:
    print('Sua categoria é:\033[;36mSENIOR. ')
else:
    print("Sua categoria é: \033[;31mMASTER. ")
