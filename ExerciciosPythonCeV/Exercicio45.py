from random import randint
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
x = randint(0,2)
print('''Escolha:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*11)
print('Computador jogou {}'.format(itens[x]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if x == 0: #PC JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('Jogada invalida')
elif x == 1: #PC JOGOU PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    else:
        print('Jogada invalida')
elif x == 2: #PC JOGOU TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')



