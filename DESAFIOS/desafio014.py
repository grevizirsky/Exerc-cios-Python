#Escreva um programa que converta uma temperatura digitada em C para F
c = float(input('Digite a temperatura em Celsius: '))

f = (c * 9/5) + 32

print('A temperatura de {}°C corresponde a {}°F'.format(c, f))