num = [[], []]
valor = 0

print('-=' * 30)
print(f'{'NÚMEROS PARES E ÍMPARES':^60}')
print('-=' * 30)
for c in range(1, 8):
    valor = int(input(f'Insira o {c}º valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
