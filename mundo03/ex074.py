from random import randint
sorteio = tuple(randint(1, 10) for _ in range(5))

print(f'Os valores sorteados foram: {sorteio}')
print(f'\nO menor valor sorteado foi {min(sorteio)}')
print(f'O maior valor sorteado foi {max(sorteio)}')
