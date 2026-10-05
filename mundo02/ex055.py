maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Insira o peso da {p}ª em kg: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'A pessoa mais pesada tem {maior:.2f}kg')
print(f'E a mais leve tem {menor:.2f}kg')
