# refaca o desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando laco for
n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
    