print('='*30)
print('{:^30}'.format('TERMOS DE UMA PA'))
print('='*30)
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = pt + (10 - 1) * razão
for c in range (pt, décimo + razão, razão):
    print('{} '.format(c), end= '> ')
print('ACABOUUU!!')