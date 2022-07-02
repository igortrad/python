n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('Sua média é {:.1f}'.format(m))
if m>= 6:
    print('Voce foi aprovado.')
else:
    print('Você foi reprovado...')