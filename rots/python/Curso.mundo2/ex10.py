from random import randint
from time import sleep
print('{:=^40}'.format(' \033[35m VAMOS JOGAR JOKEMPO? \033[m '))
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''VOCÊ TEM AS OPÇÃO!!!
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
sleep(1)
print('-=-' * 20)
print('O computador escolheu {} '.format(itens[computador]))
print('O jogador escolheu {} '.format(itens[jogador]))
print('-=-' * 20)
if computador == 0: #pedra
    if jogador == 0:
        print('\033[31mEMPATOU!')
    elif jogador == 1:
        print('\033[31mO JOGADOR VENCEU!!')
    elif jogador == 2:
        print('\033[31mO COMPUTADOR VENCEU!!!')
    else:
        print('\033[31mJOGADA INVALIDA, TENTE NOVAMENTE!!')
elif computador == 1:
    if jogador == 0:
        print('\033[31m COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('\033[31m EMPATOU!!')
    elif jogador == 2:
        print('\033[31m O JOGADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA, TENTE NOVAMENTE!!!')
elif computador == 2:
    if jogador == 0:
        print('\033[31m O JOGADOR VENCEU!!')
    elif jogador == 1:
        print('\033[31m O COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print('\033[31m EMPATOU!!')
    else:
        print('JOGADA INVALIDA, TENTE NOVAMENTE!!!')


