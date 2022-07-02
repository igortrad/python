casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos voce quer pagar a casa? '))
parcela = casa / (anos * 12)
if parcela >= (30/100 * salario):
    print('Infelizmente o parcelamento foi NEGADO.')
else:
    print('Parabens, seu parcelamento foi aprovado!')
    print('Voce vai pagar {:.0f} durante {} anos'.format(parcela, anos))
