# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('É um palindromo')
else:
    print('Não é um palindromo')