# faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input('Qual é o salario? R$ '))

aumento = salario + (salario * 15 / 100)

print('Um funcionario que ganhava R${}, com 15% de aumento, passa a receber R${}'.format(salario, aumento))