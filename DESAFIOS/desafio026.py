# Faca um programa que leia a frase pelo teclado e mostre: Quantas vezes aparece a letra "a"; Em que posicao ela aparece a primeira vez; Em que posicao ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A') + 1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A') + 1))
