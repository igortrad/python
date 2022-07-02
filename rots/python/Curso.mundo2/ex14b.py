from random import randint
computador = randint(0,10)
print('Sou seu computador...\nacabei de pensar em um número de 0 a 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais, tente novamente!')
        elif jogador > computador:
            print('menos, tente novamente!')
print('Acertou com {} palpites, parabénsss!!'.format(palpites))
