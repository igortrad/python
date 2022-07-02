dist = float(input('Qual a distancia da viagem em km? '))
print('Você está prestes a começar sua viagem de {}Km'.format(dist))
if dist <= 200:
    print('Sua passagem vai custar R${}'.format(dist*0.5))
else:
    print('Sua passagem vai custar R${}'.format(dist*0.45))