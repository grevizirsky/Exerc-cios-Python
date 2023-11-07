# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas
km = float(input('Qual a distancia em Km? '))
print('Voce esta prestes a comecar uma viagem de {}Km'.format(km))

if km <= 200:
    preco = km * 0.50
else: 
    preco = km * 0.45

print('O preço da passagem é de R${:.2f}'.format(preco))