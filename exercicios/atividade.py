import os

def validade_user(username, password):
    stored_user = os.getenv('USERNAME')
    stored_pass = os.getenv('PASSWORD')
    return username == stored_user and password == stored_pass

user_input = input('Enter username: ')
pass_input = input('Enter paswword: ')

if validade_user(user_input, pass_input):
    print('Acesso concedido')
else:
    print('Acesso negado')
