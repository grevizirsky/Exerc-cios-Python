# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR
import math
n = int(input('Digite um numero: '))

resta = n % 2

if resta == 1: 
    print('O numero {} é IMPAR'.format(n))
else:
    print('O numero {} é PAR'.format(n))