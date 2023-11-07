# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O progama devera escrever na tela se o usuario venceu ou nao  
from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei? '))

if jogador == computador:
    print('Parabens, voce acertou!')
else: 
    print('Ganhei! Eu pensei no numero {} e nao no {}'.format(computador, jogador))

