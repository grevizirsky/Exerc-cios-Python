# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

n1 = input('Digite algo: ')

print(type(n1))
print('É alfanumerico? ', n1.isalnum())
print('Contem apenas letras do alfabeto? ', n1.isalpha())
print('Contem apenas ASCII? ', n1.isascii())
print('É decimal? ', n1.isdecimal())
print('É um digito? ', n1.isdigit())
print('É um identificador valido? ', n1.isidentifier())
print('Esta em caixa baixa? ', n1.islower())
print('Esta em caixa alta? ', n1.isupper())
print('É numerico? ', n1.isnumeric())
print('Todos os caracteres sao imprimiveis? ', n1.isprintable())
print('Contem apenas espaço em branco? ', n1.isspace())
print('Segue o formato de titulo? ', n1.istitle())
