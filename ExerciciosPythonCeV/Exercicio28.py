from random import randint
pc = randint(0, 5)
n = int(input('Digite um numero de 0 a 5: '))
if n == pc:
    print('PARABENS, Você ganhou!')
else:
    print('Você perdeu...')

