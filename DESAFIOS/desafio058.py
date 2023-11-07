# melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um numero entre 0 e 10, so que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint
computador = randint(0, 10)
palpites = 0
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei? '))

while jogador != computador:
    if computador > jogador:
        jogador = int(input('Mais... tente novamente: '))
    else:
        jogador = int(input('Menos... tente novamente: '))
    palpites += 1
print('Parabens, voce acertou! Voce fez {} palpites'.format(palpites + 1))
