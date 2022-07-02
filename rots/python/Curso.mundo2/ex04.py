'''faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se ja passou do tempo de alistamento
seu programa também mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {} '.format(nasc,idade,atual))
if idade == 18:
    print('Você deve se alistar imediatamente ')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + idade
    print('Você ainda não tem 18 anos, ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} '.format(ano))

elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos '.format(saldo))
    print('Seu alistamento foi em {} '.format(ano))
