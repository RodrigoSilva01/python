while True:
    num = int(input('Insira um número para ver sua tabuada (NÚMEROS NEGATIVOS PARA ENCERRAR): '))
    if num < 0:
        break

    print('-' * 15)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-' * 15)      
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
