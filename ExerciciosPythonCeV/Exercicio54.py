from datetime import date
atual = date.today().year
tma = 0
tmen = 0
for pes in range (1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pes)))
    idade = atual - nasc
    if idade >= 18:
        tma += 1
    else:
        tmen += 1
print('{} pessoa(s) menores de idade e {} maiore(s) de idade.'.format(tmen, tma))
