# refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado: equilatero: todos os lados iguais; isosceles: dois lados iguais; escaleno: todos os lados diferentes
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar triangulo ', end='')
    if s1 == s2 and s2 == s3:
        print('EQUILATERO')
    elif s2 != s2 and s2 != s3 and s1 != s3:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Os segmentos acima NAO podem formar triangulo')