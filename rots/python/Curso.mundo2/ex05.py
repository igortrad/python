'''
crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
 no final de acordo com a media atingida
media abaixa de 5.0 REPROVADO
media entre 5.0 e 6.9 recuperação
Media de 7.0 ou superior APROVADO'''

n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
soma = (n1 + n2) / 2
print('Com a nota {} e {} a média do aluno é {} '.format(n1,n2,soma))
if soma < 5:
    print('Você está \033[31mREPROVADO!!!')
elif 7 > soma >= 5:
    print('Você está de \033[31mRECUPERAÇÃO!!!')
elif soma >= 7:
    print('Parabéns você foi \033[31mAPROVADO!!!')