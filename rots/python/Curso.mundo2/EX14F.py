print('GERADOR DE PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termo você quer ver mais? '))
print('Foi mostrando {} termos de progressão '.format(total))