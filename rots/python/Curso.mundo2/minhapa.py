print('-=-'* 15 )
print('\033[31mprogressão de PA\033[m')
print('-=-' * 15)
primeiro = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos de PA você quer ver mais? '))
print('\033[34m Foi mostrado {} termos de PA'.format(total))