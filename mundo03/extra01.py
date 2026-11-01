inventario = []
temp = []
totpreco = maior = menor = 0
caro = barato = ''

while True:
    temp.append(str(input('Insira o nome do produto: ')))
    temp.append(float(input('Insira o preço do produto: ')))

    totpreco = totpreco + temp[1]

    if len(inventario) == 0:
        maior = menor = temp[1]
        caro = barato = temp[0]
    else:
        if temp[1] >= maior:
            maior = temp[1]
            caro = temp[0]
        if temp[1] <= menor:
            menor = temp[1]
            barato = temp[0]

    inventario.append(temp[:])
    temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

for i, c in enumerate(inventario):
    print(f'{i + 1:<2} {c[0]:.<33} R${c[1]:>8.2f}')

print('-' * 50)
print(f'Foram cadastrados {len(inventario)} produtos')
print(f'O produto mais caro foi {caro} custando R${maior:.2f}')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')
print(f'A média de preço dos produtos é R${totpreco / len(inventario):.2f}')
print('-' * 50)
