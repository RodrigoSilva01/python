tot_gasto = cont = sup100 = menor = 0
barato = ''

print('-' * 55)
print(f'{'SISTEMA DE CONTROLE DE VENDAS':^55}')
print('-' * 55)
while True:
    produto = str(input('Insira o nome do produto: ')).strip()
    
    while True:
        try:
            preco = float(input('Insira o preço do produto: R$'))
            break
        except ValueError:
            print('Preço inválido! Digite apenas números (ex: 15.50).')

    cont = cont + 1
    tot_gasto = tot_gasto + preco

    if preco > 100:
        sup100 = sup100 + 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 55)
print(f'O preço total dos produtos é de: R${tot_gasto:.2f}')
print(f'Existem {sup100} produtos que custam mais que R$100.00')
print(f'O produto mais barato é {barato} e custa R${menor:.2f}')
print('-' * 55)
