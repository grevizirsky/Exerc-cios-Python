# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 1 para binario, 2 para octal, 3 para hexadecimal
num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:\n [ 1 ] converter para BINARIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido pra BINARIO é igual a {}'.format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} convertido pra OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} convertido pra HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Por favor digite uma das opcoes acima')
