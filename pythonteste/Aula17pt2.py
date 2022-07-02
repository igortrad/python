teste = list()
teste.append('Gian')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#Para ler nomes e colocar na lista
galera = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

#Para ver se é maior de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]} é maior de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade. ')