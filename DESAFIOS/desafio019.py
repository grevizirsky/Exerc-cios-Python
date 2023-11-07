# um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles 
# e escrevendo o nome do escolhido
import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

randomizar = random.choice(lista)

print('O nome escolhido foi: {}'.format(randomizar))