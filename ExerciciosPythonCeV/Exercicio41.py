from datetime import date
nasc = int(input('Qual o ano de nascimento do atleta? '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <=19:
    print('CATEGORIA JUNIOR')
elif idade <= 25:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')
