from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasci = int(input('Digite o ano do seu nascimento da {}° pessoa: '.format(pess)))
    idade = atual - nasci
    if idade >= 21:
      totmaior += 1
    else:
         totmenor += 1
print('Ao todo tivemos {} pessoas maiores. '.format(totmaior))
print('E também tivemos {} pessoas menores. '.format(totmenor))


