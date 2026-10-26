valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 50)
print(f'Você digitou {len(valores)} números.')

valores.sort(reverse=True)
print(f'Os números na ordem decrescente é {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
