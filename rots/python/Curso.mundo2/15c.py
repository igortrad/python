from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} e o total é {total}')
    print('DEU IMPAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou!!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos jogar novamente....')
print(f'GAMER OVER! você venceu {v} vezes')