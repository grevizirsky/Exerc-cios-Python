# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; 25 ate 30: sobrepeso; 30 ate 40: obesidade; acima de 40: obesidade morbida
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Voce esta NA FAIXA do peso normal')
elif imc >= 25 and imc < 30:
    print('Voce esta em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Voce esta em OBESIDADE, cuidado!')
elif imc >= 40: 
    print('Voce esta em OBESIDADE MORBIDA')