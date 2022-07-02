times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
      'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
      'Atletico-MG', 'Botafogo', 'Athletico-PR', 'Bahia',
      'São Paulo', 'Fluminense', 'Sport', 'Vitoria',
      'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
print('-='*50)
print(f'Lista de times: {times}')
print('-='*50)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-='*50)
print(f'Os quatro ultimos colocados são: {times[16:]}')
print('-='*50)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*20)
print(f'A Chape esta na posição {(times.index("Chapecoense")+1)}')
print('-='*20)


