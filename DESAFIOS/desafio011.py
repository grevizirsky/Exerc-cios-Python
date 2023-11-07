#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, 
#sabendo que cada litro de tinta pinta uma area de 2m^2 
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua area é {}m^2'.format(largura, altura, area))

litro = area / 2

print('Para pintar essa parede, voce precisará de {}L de tinta'.format(litro))