soma = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma = soma + num 
print(f'A soma dos números pares, desconsiderando os impares é {soma}')
