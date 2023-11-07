# faca um programa que leia um numero qualquer e mostre o seu fatorial. Ex: 5!=5x4x4x3x2x1=120
#from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
count = n
f = 1
print('Calculando {}! = '.format(n), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
#f = factorial(n)
print('{}'.format(f))