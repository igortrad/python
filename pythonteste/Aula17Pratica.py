#num = [2, 5, 8, 3, 1]
#num.append(7)
#num.sort()
#print(num)
#print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(6)
for cont in range (0, 7):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')