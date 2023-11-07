# a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: ate 9 anos: mirim; ate 14 anos: infantil; ate 19 anos: junior; ate 20 anos: senior; acima: master
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 20:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')