#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0 com uma pause de 1 segudno entre eles]
print('Contagem regressiva para o fim do ano!!!!')
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[31m BUMMMMMMMMMMMM')