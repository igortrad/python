from random import randint
pc = randint(0, 10)
print('Sou seu computador ... Acabei de pensar em um numero de 0 a 10.')
print('Será que você consegue adivinhar? ')
n = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    n += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou!')
print('Você precisou de {} chances para acertar. '.format(n))
