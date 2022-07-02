f = input('Digite a frase: ').strip().upper()
palavras = f.split() #SEPAREI EM PARTES A FRASE
junto = ''.join(palavras) #JUNTEI AS PALAVRAS
inverso = ''
#outra forma é inverso = junt[::-1] eliminando o for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')

