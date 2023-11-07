# crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida: Media abaixo de 5: reprovado; media entre 5 e 6.9: recuperacao; media 7 ou superior: aprovado
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a media do aluno é {}'.format(n1, n2, media))
if media < 5:
    print('O aluno esta REPROVADO')
elif media >= 5 and media <= 7:
    print('O aluno esta de RECUPERACAO')
elif media >= 7:
    print('O aluno esta APROVADO')