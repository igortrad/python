num = (int(input('Digite o primeiro numero: ')),
       int(input('Digite o segundo numero: ')),
       int(input('Digite o terceiro numero: ')),
       int(input('Digite o quarto numero: ')))
print(num)
print(f'O numero nove apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero três foi digitado pela primeira vez na posição {num.index(3)+1}')
else:
    print('Não tem nenhum numero três. ')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')