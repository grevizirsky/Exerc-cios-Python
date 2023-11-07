#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiusculas; O nome com todas minusculas; Quantas letras ao todo (sem considerar espacos); Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))