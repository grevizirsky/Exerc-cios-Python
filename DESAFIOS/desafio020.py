# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatros
# alunos e mostre a ordem sorteada
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('A ordem de apresentacao será')
print(lista)