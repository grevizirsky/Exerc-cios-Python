#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um numero: '))

print('o dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))