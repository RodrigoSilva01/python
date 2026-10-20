print('=' * 30)
print(f'{'BANCO RSS':^30}')
print('=' * 30)

while True:
    valor = int(input('Que valor você quer sacar? R$'))

    tot50 = valor // 50
    resto = valor % 50
    tot20 = resto // 20
    resto = resto % 20
    tot10 = resto // 10
    resto = resto % 10
    tot01 = resto // 1

    print(f'Total de {tot50} cédulas de R$50')
    print(f'Total de {tot20} cédulas de R$20')
    print(f'Total de {tot10} cédulas de R$10')
    print(f'Total de {tot01} cédulas de R$1')
    print('=' * 30)

    resp = str(input('Quer fazer outro saque? [S/N] ')).strip().upper()
    if resp == 'N':
        break
    
print('Volte sempre ao BANCO RSS! Tenha um bom dia!')
