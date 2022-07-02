'''a conferação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre a sua categoria de acordo com sua idade
até 9 anos : mirim
até 14 anos : infantil
19 anos : junior
20 anos : senhor
acima master'''

from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
ano = atual - nascimento
if ano < 9:
    print('Você é um atleta \033[31mMIRIM!!!')
elif 9 > ano < 14:
    print('Você é um atleta \033[31mINFANTIL!!!')
elif 14 > ano < 20:
    print('Você é um atleta \033[31mJUNIOR!!')
elif ano == 20:
    print('Você é um atleta \033[31mSENIOR!!!')
else:
    print('Você é um atleta \033[31mMASTER!!!')