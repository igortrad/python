'''1- Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'm' ou 'f'.
caso esteja errado, peça a digitação novamente até ter um valor correto
'''
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidados, por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso! '.format(sexo))