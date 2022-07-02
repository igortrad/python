import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))