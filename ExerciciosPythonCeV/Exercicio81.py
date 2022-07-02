lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = input('Quer continuar? [S/N]')
    if r in 'Nn':
        break
print('-='*30)
print(f'Foram adicionados {len(lista)} valores a lista.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado')


