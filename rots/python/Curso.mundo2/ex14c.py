from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros 
    [ 5 ] sair do programa''')
    opção = int(input('Qual é sua opção? '))
    print('-=-'*10)
    if opção == 1:
        soma = n1 + n2
        print('a soma entre {} + {} é igual {}'.format(n1,n2,soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação enter {} x {} é {}'.format(n1,n2,multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opção == 4:
        n1 = int(input('Primeiro valor:  '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('O programa está sendo finalizado!!')
        sleep(3)
        print('Volte sempre!!')
    else:
        print('condigo invalido, digite novamente!')