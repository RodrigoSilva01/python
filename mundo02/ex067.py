num = 0

while True:
    num = int(input('Insira um número para ver sua tabuada (NÚMEROS NEGATIVOS PARA ENCERRAR): '))
    if num < 0:
        break
    
    for cont in range(1, 11):
        multi = num * cont
        print(f'{num} x {cont} = {multi}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
