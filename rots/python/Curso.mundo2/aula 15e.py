print('-'*20)
print('Loja Super Baratão')
print('-'*20)
totc = cont = mil = menor = 0
barato = ''
while True:
    nome_produto = str(input('Nome do produto : '))
    preço = float(input('Preço do produto: R$ '))
    cont += 1
    totc = totc + preço
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome_produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto é R$ {totc :.2f}')
print(f'Temos {mil} produtos são acima de R$ 1000,00 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')