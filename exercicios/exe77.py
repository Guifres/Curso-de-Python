print('=' * 40)
palavras = ('programar', 'phyton', 'gratis', 'curso',
          'video', 'estudar', 'futuro', 'conhecimento',
          'aprender')
for c in palavras:
    print(f'\nTemos na palavra {c.upper()} essas Vogais: ', end='')
    for letras in c:
        if letras in 'aeiou':
            print(letras.lower(), end='')
