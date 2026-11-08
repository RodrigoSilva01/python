from time import sleep
from random import randint
from operator import itemgetter

jogo = {}

print('Valores sorteados: ')
for c in range(1, 5):
    dado = randint(1, 6)
    jogo[f'jogador{c}'] = dado
    print(f'   Jogador{c} tirou {dado} no dado.')
    sleep(0.5)

print('-=' * 35)
print('  == RANKING DOS JOGADORES ==')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
