'''elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
a vista dinheiro/cheque: 10% de desconto
a vista no cartão: 5% de desconto
em até 2x no cartão : preço normal
3x no cartão : 20% de juros
]'''

produto = float(input('Qual o valor do produto? '))
print('''Qual é a forma de pagamento?
[1] A vista dinheiro ou Cheque (10% de desconto)
[2] A vista no cartão (5% de desconto)
[3] em até 2x no cartão?(preço normal)
[4] 3x no cartão? (20% de juros) ''')
opcao = int(input('Sua opção? '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
    print('com o valor do produto {}, com 10% de desconto você pagara {} '.format(produto, total))
elif opcao == 2:
    total = produto - (produto * 5 / 100)
    print('O preço do produto é {} e com 5% de desconto você pagara {} '.format(produto, total))
elif opcao == 3:
    print('O preço do produto é {} e você não tem descontos!!!'.format(produto))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totalparc = int(input('Em quantas parcelas vai parcelar? '))
    print('Parcelando em {}x você tera 20% de JUROS!!'.format(totalparc))
    print('O produto que era R$ {:.2f} vai sair por R$ {:.2f}'.format(produto, total))
else:
    total = 0
    print('\033[31m OPÇÃO INVALIDA DE PAGAMENTO!!')
    print('Tente novamente')