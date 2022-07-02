c = ('zero','um', 'dois','três','quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'catorze', 'quinzez',
     'dezesseis', 'dezessete', 'dezoito', 'dezenove',
     'vinte')
while True:
     escolha = int(input('Escolha um numero de 0 a 20: '))
     if 0 <= escolha <= 20:
          break
     print('Tente Novamente burrão ', end='')
print(f'Voce digitou o numero {c[escolha]}')