soma = 0
for _ in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num 
print(f'A soma dos números pares, desconsiderando os impares é {soma}')
