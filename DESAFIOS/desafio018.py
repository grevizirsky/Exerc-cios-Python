# faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan))