# faca um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto
produto = float(input('Qual é o preço do produto: '))

desconto =  produto - (produto * 5 / 100)

print('O produto que custava R${} na promoção com desconto de 5% vai custar R${}'.format(produto, desconto))