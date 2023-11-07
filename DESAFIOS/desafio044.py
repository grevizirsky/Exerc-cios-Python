# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento: a vista dinheiro/cheque:10% de desconto; a vista no cartao: 5% de desconto; em ate 2x no cartao: preco normal; 3x ou mais no cartao: 20% de juros
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartao''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_parcela
    if total_parcela >= 3:
        print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcela, parcela))
    if total_parcela == 2:
        print('Sua compra sera parcelada em 2x de R${:.2f} COM JUROS'.format(parcela))
    if total_parcela == 1:
        print('Sua compra sera parcelada em 1x de R${}'.format(preco))
else: 
    print('OPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))