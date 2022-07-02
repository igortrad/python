'''

escreva um programa que leia dois numeros inteiros e compare os mostrando na tela uma mensagem
 o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 < n2:
    print('O Segundo numero {} é maior que o primeiro numero {}'.format(n2,n1))
elif n1 > n2:
    print('O primeiro numero {} é maior que o segundo numero {}'.format(n1, n2))
else:
    print('Nenhum numero é maior, os dois são IGUAIS')