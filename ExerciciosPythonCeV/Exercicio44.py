preco = float(input('Digite o preço normal do produto: '))
cond = int(input('''Escolha uma das opções de pagamento:
[ 1 ] Dinheiro ou Cheque (10% de Desconto)
[ 2 ] A Vista no cartão  ( 5% de Desconto)
[ 3 ] Em até 2x no cartão (Preço Normal)
[ 4 ] Em 3x ou mais no cartão (20% de juros)
'''))
av = preco - (preco * 10/100)
ac = preco - (preco * 5/100)
tv = preco + (preco * 20/100)
if cond == 1:
    print('Você vai pagar {} pelo produto.'.format(av))
elif cond == 2:
    print('Você vai pagar {} pelo produto.'.format(ac))
elif cond == 3:
    print('Você vai pagar {} pelo produto.'.format(preco))
elif cond == 4:
    print('Você vai pagar {} pelo produto.'.format(tv))
else:
    print('Você digitou uma opção inexistente. Tente novamente.')

