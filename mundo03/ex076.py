listagem = ('Pão', 0.50, 'Arroz', 7.60, 'Feijão', 8.55, 'Pizza', 60.59, 'Manteiga', 19.99, 'Refrigerante', 12.66, 'Café', 23.99, 'Picanha', 120.90, 'abacate', 2.00)

print('-' * 41)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 41)

for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30} R${listagem[pos + 1]:>7.2f}')
print('-' * 41)
