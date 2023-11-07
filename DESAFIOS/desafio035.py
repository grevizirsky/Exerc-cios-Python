# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar triangulo')
else:
    print('Os segmentos acima NAO podem formar triangulo')