# crie um programa que leia dois valores e mostre um menu na tela: [1] somar; [2] multiplicar; [3] maior; [4] novos numeros; [5] sair do programa. Seu programa devera realizar a operação solicitada em cada caso
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] somar 
[2] multiplicar 
[3] maior 
[4] novos numeros 
[5] sair do programa
''')
    opcao = int(input('Qual sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('{} x {} é {}'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print('Entre {} e {} o maior numero é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opcao invalida, tente novamente')
 
print('Fim do programa')