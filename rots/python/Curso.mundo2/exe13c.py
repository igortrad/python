numero = int(input('Digite um numero para ver a tabuada? '))
print('-=-' * 20)
for c in range (1, 11):
    print('{} x {:2} = \033[34m{}\033[m '.format(numero, c, numero*c))
print('-=-' * 20)