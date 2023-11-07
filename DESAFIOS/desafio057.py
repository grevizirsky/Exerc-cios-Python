# faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. Caso esteja errado, peça a digitacao novamente até ter um valor correto
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]#[0] pega somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, digite seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))