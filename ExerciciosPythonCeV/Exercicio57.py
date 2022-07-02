sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalidos, por favor informe o sexo novamente: [M/F] ')
print('Dado validado com sucesso')