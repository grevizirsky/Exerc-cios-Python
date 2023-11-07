# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior; o segundo valor é maior; nao existe valor maior, os dois sao iguais
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('o PRIMEIRO valor é maior')
elif n2 > n1:
    print('o SEGUNDO valor é maior')
else:
    print('Nao existe valor maior, os dois sao iguais ')