# crie um programa que faca o computadopr jogar jokenpo com voce
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0:#computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Jogador PERDEU')
    else:
        print('Jogada invalida')
elif computador == 1:#computador jogou PAPEL
    if jogador == 0:
        print('Jogador PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:#computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Jogador PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')