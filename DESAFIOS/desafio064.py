# crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = 0
n = int(input('Digite um numero inteiro [999 para parar]: ')) 
count = 0
soma = 0
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um numero inteiro [999 para parar]: '))    
print('Voce digitou {} numeros e a somaa entre eles foi {}'.format(count, soma))
