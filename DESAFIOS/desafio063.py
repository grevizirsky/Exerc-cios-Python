# escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci. Ex: 0->1->1->2->3->5->8
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} - {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1