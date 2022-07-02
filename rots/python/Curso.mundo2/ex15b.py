print('-'* 20)
print('\033[31mPrograma de tabuada\033[m')
print('-' * 20)
while True :
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n  < 0:
        break
    for tabuada in range (1,11):
        print(f'{n} X {tabuada} = {n*tabuada} ')
print('Tabuada finalizada!')