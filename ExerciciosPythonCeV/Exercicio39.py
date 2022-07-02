from datetime import date
nome = input('Qual o seu nome? ')
ano = int(input('Que ano você nasceu? '))
anoa = date.today().year
idade = anoa - ano

if idade < 18:
    falta = 18-idade
    print('{}, voce ainda vai se alistar no serviço militar daqui {} anos'.format(nome, falta))
elif idade == 18:
    print('{}, está na hora de voce se alistar no serviço militar!'.format(nome))
else:
    passou = idade-18
    print('{}, você já deve ter se alistado no serviço militar a {} anos'.format(nome, passou))