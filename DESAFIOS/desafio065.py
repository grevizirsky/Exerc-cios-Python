# crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
def contador_decrescente(inicio, fim):
    for numero in range(inicio, fim - 1, -1):
        print(numero)

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

contador_decrescente(inicio, fim)