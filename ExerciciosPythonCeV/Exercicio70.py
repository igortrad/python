preco = pr1000 = cont = 0
barato = ''
while True:
    nome = input('Nome do Produto: ')
    pr = float(input('Preço do Produto: R$ '))
    cont += 1
    preco += pr
    if pr > 1000:
        pr1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' COMPRA FINALIZADA '))
print(f'Voce gastou {preco} reais,')
print(f'{pr1000} produto(s) custa mais de R$1000. ')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
