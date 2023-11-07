#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor
n1 = int(input('Digite um numero: '))
sucessor = n1 + 1
antecessor = n1 - 1

print('O numero sucessor ao {} é {} e o antecessor é {}'.format(n1, sucessor, antecessor))