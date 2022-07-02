peso = float(input('Digite seu PESO: '))
altura = float(input('Digite sua ALTURA: '))
imc = peso/(altura*altura)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso. ')
elif 18.5 <= imc < 25:
    print('Você esta no PESO IDEAL. ')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')