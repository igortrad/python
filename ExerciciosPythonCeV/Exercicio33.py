a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))
#verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and b>c:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


