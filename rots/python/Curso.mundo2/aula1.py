nome = str(input('Qual é seu nome?')).strip()
if nome == 'igor':
    print('Você tem um belo nome ')
elif nome in 'pedro ana carlos mauricio barnabe':
    print('Seu nome é bem popular no Brasil ')
elif nome == 'flavia' or nome == 'gian' or nome == 'thiago':
    print('Seu nome é bonito')
else:
    print('Seu nome é bem normal ')
print('\033\3m tenha um bom dia')