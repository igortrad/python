listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15,
            'Estojo', 7)
print('-' * 15)
print('LISTA DE PREÇOS')
print('-' * 15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')