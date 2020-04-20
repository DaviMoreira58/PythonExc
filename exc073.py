# Crie um tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de
# futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados na tabela.
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense

"""tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético - MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco',
          'Sport', 'América-MG', 'Vitória', 'Paraná Clube')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 30)
print(f'Os 5 primeiros: {tabela[:5]}')
print('-=' * 30)
print(f'Os 4 ultimos: {tabela[-4:]}')
print('-=' * 30)
print(f'Em ordem alfabética: {sorted(tabela)}')
print('-=' * 30)
pos = tabela.index('Chapecoense')
print(f'A Chapecoense está na {pos}ª posição')
print('-=' * 30)""" # Meu jeito

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético - MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco',
          'Sport', 'América-MG', 'Vitória', 'Paraná Clube')
print('-=' * 15)
print(f'Lista de times: {times}') # for t in times: print(f'{t}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
