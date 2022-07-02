num = int(input('Escolha um numero para saber a sua tabuada: '))
for t in range (1, 11):
    print('{} x {} = {}'.format(num, t, num*t))