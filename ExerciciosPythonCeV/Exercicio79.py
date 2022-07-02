numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Numero ja esta na lista, tente novamente.')
    r = input('Quer continuar? [S/N]')
    if r in 'Nn':
        break
print('-='*25)
numeros.sort()
print(f'Voce adicionou os valores: {numeros}')