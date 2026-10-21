tot_gasto = contador = menor = sup1000 = 0
barato = ''

print('-' * 40)
print(f'{'LOJAS RODRIGUES':^40}')
print('-' * 40)

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    
    contador = contador + 1
    tot_gasto = tot_gasto + preco
    
    if preco > 1000:
        sup1000 = sup1000 + 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^50}')
print(f'O total da compra foi R${tot_gasto:.2f}')
print(f'Temos {sup1000} produto(s) custando mais que R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
