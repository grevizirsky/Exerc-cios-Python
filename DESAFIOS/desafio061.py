# refaca o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
while count <= 10:
    print('{}'.format(termo))
    termo += razao
    count += 1
print('Acabou')