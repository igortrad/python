from random import randint
n = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(n)
print(f'O maior valor na tupla é {max(n)}')
print(f'O menor valor na tupla é {min(n)}')