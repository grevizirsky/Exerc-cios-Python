nome = str(input('Qual ée seu nome? '))
if nome == 'Adriano':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem poppular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))