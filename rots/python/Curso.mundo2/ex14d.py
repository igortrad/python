#from math import factorial
#numero = int(input('Digite um número para calcular seu fatorial: '))
#fatorial = factorial(numero)
#print('O fatorial do número {} é {} '.format(numero,fatorial))

#WHILE!
#n = int(input('Digite um número para calcular seu fatorial: '))
#c = n
#f = 1
#print('Calculando {}! = '.format(n), end='')
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f = f * c
#    c -= 1
#print('{}'.format(f))

n = int(input('Digite um número para calcular seu fatorial:'))
c = n
f = 1
for c in range (1,6):
    f = f * c
    print('O Fatorial de {} é {}'.format(n,f))