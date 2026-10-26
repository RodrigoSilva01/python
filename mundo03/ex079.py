numeros = []

while True:
    n = int(input('Insira um número: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 60)
numeros.sort()
print(f'Você adicionou os valores: {numeros}')
