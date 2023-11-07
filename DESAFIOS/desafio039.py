# faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar ao servico militar, se é a hora de se alistar, se ja passou do tempo do alistamento. Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo 
from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos pro alistamento'.format(saldo)) 
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
