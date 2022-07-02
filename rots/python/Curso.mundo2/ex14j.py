resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
        num = int(input('Digite um numero: '))
        soma += num
        quant += 1
        if quant == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('você digitou {} números e a media entre eles é {} '.format(quant, media))
print('O maior número é {} e o menor é {}'.format(maior,menor))