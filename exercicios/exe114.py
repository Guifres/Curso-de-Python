import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('O site não esta acessivel')
else:
    print('o site esta acessivel')
    print(site.read())