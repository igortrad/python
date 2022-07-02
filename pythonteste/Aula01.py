nome = input('Qual é o seu nome? ')
if nome == 'Gian':
    print('Gostoso')
elif nome == 'Ana' or nome == 'Julio' or nome == 'Paulo':
    print('Seu nome é comum')
elif nome in ' Danilo, Raul, Luci, Pantera':
    print('Criativa')
else:
    print('Horrivel')
print('Tenha um bom dia, {}'.format(nome))
