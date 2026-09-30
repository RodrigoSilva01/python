maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Insira seu peso em kg: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'A pessoa mais pesada tem {maior:.2f}kg')
print(f'E a mais leve tem {menor:.2f}kg')
