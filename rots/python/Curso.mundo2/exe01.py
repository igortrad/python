#exe 1 escreva um programa para aprovar o emprestimo bancaria para compra de uma casa.
# o programa vai pergunta o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salari ou então o emprestimo
# sera negado.]



print('-=-' * 20 )
print('Bem-vindo ao programa de simulação de emprestimo bancario')
print('-=-' * 20)
casa = float(input('Qual é o valor da casa? R$: '))
salario = float(input('Qual é o salario mensal? R$: '))
anos = int(input('Em quantos anos pretende pagar?'))
prestação = casa / (anos * 12 )
minimo = salario * 30 / 100
print('Com o valor da casa R$ {:.2f} em {:.2f} anos, a prestação fica a R$ {:.2f} por mes '.format(casa,anos,prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!!!')
else:
    print('Emprestimo NEGADO!!!')