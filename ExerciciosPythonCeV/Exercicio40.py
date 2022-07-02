n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
m = (n1 + n2)/2
if m < 5:
    print('Você foi REPROVADO')
elif m > 7:
    print('Voce foi APROVADO')
else:
    print('Você esta de RECUPERAÇÃO')