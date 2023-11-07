#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = m * 1000

print('A conversão de metros pra centimetros é {:.0f}cm e pra milimetros é {:.0f}mm'.format(cm, mm))
