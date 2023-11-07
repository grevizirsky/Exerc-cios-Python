# melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0: #enquanto 'mais' for diferente de 0 sera executado
    total = total + mais
    while count <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        count += 1
    print('Pausa') 
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('FIM')