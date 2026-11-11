jogador  = {}
partidas = []

jogador["nome"] = str(input('Qual o nome do jogador? '))
tot_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, tot_partidas):
    gols = int(input(f'Quantos gols na partida {c + 1}? '))
    partidas.append(gols)

jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)

print('-' * 100)
print(jogador)
print('-' * 100)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 100)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
print('-' * 100)
