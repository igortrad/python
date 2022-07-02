n1 = int(input('PRIMEIRO VALOR: '))
n2 = int(input('SEGUNDO VALOR: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre os dois numeros é {}'.format(n1+n2))
    elif opcao == 2:
        print('A multiplicação entre os dois numeros é {}'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é o {}'.format(maior))
    elif opcao == 4:
        print('Informe os numeros novamente. ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida')
    print('=-=' * 10)
print('Fim do Programa.')
