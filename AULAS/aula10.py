'''nome = str(input('Qual seu nome? '))
if nome == 'Adriano':
    print('Que nome lindo voce tem!')
else: 
    print('Que nome normal voce tem')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
m = (n1 + n2) / 2
print('Sua media foi {}'.format(m))
if m >= 6.0:
    print('Sua media foi muito boa, PARABENS!')
else: 
    print('Sua media foi ruim, ESTUDE MAIS!')
