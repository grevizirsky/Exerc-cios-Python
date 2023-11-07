# Faca um programa que leia tres numeros e mostre qual é o maior e qual é o menor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))
