cont = ('zero', 'um', 'dois', 'tres', 'quatro', ' cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 á 20: '))
    if 0 <= num <= 20:
        break
    print(' Tente novamente, ', end='')
print(f'Você digitou o número {cont[num]}')