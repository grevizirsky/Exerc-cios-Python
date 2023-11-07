# crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira
from math import trunc
num = float(input('Digite um numero: '))

porcao = trunc(num)

print('O numero {} tem a parte inteira {}'.format(num, porcao))