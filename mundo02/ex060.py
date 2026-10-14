num = int(input('Insira um número para calcular seu Fatorial: '))
cont = num
resultado = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end='')
    resultado = resultado * cont
    cont = cont - 1
print(f'{resultado}')
