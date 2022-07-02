lanche = ('Hamburguer', 'Suco','Pizza', 'Pudim')
#maneira 1
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#maneira 2
for comida in lanche:
    print(f'Eu vou comer {comida}')

#se precisar da posição
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#ou
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Somando Tuplas
a = (2, 5, 6)
b = (3, 9, 10)
c = a + b
print(c)

#Contando elementos da tupla
a = (2, 5, 6)
b = (3, 9, 10)
c = a + b
print(len(c))

#Contando quantas vezs aparece tal elemento
a = (2, 5, 6)
b = (3, 9, 10)
c = a + b
print(c.count(5))

#Posição de tal numero
a = (2, 5, 6)
b = (3, 9, 10)
c = a + b
print(c)
print(c.index(5))

#apagando a tupla

pessoa = ('Gian', 25, 'M', 100)
del(pessoa)