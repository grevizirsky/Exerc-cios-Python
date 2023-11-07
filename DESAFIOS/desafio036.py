# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa, o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado
valor = float(input('Valor da casa: R$ '))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * 30 / 100

prestacao = valor / (anos * 12)


print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestacao sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser concedido')
else: 
    print('Emprestimo negado ')