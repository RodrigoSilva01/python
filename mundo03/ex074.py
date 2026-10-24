from random import randint

sorteio = tuple(randint(1, 10) for _ in range(5))
print('Os valores sortados foram: ', end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi {min(sorteio)}')
print(f'O maior valor sorteado foi {max(sorteio)}')
