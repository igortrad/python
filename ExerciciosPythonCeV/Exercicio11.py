l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
print('A area da parede é de {:.3f}m²'.format(ar))
tinta = ar / 2
print('Para pintar a parece, voce precisara de {}l de tinta'.format(tinta))