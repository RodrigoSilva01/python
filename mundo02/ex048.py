s = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c
print(f' a soma dos valores que são impares e multiplos de 3 é {s}')
print('FIM!')
