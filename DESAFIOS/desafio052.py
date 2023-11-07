# faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c)
print('\033[mO numero {} foi divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('É primo')
else:
    print('Não é primo')
    