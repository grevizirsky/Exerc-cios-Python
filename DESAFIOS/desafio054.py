# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores'.format(totmaior, totmenor))