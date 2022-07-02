'''
refaça o desafio 035 dos trinagulhos, acrescentando o recurso de mostrar que tipio de
 triangulho será formado
equilatero: todos os lados iguais
isosceles: dois lados iguais
escaleno: todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!', end='')
    if r1 == r2 and r2 == r3:
        print(' EQUILATERO')
    elif r1 != r2 and r3 != r1:
        print('ESCALENO!')
    else:
       print('ISÓSCELES')
