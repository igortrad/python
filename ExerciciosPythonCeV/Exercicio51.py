pa = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
decimo = pa + (10-1)*r
for c in range (pa, decimo, r):
    print('{}'.format(c), end='-> ')
print ('FIM')
