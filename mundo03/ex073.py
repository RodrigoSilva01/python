times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Cruzeiro', 'Fluminense', 'Atlético-MG', 'bahia', 'Santos', 'São Paulo', 'Bragantino', 'Botafogo', 'Coritiba', 'Vitória', 'Mirassol', 'Vasco', 'Corinthians', 'Internacional', 'Grêmio', 'Remo', 'Chapecoense')

print(f'Lista dos times do Brasileirão: {times}\n')
print(f'Os 5 primeiros são: {times[:5]}\n')
print(f'Os 4 ultimos são: {times[-4:]}\n')
print(f'Times em ordem alfabética: {sorted(times)}\n')
print(f'A Chapecoense está na {times.index('Chapecoense') + 1}ª posição')
