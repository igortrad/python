n = 0
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar] : '))
while n != 999:
    cont += 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar] : '))
print('Você Digitou {} e a soma entre eles é {}'.format(cont,soma))