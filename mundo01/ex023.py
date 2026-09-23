num = int(input('Digite um número: '))

print(15 * '-')
print(f'A unidade é: {num // 1 % 10}')
print(f'A dezena é: {num // 10 % 10}')
print(f'A centena é: {num // 100 % 10}')
print(f'O milhar é: {num // 1000 % 10}')
print(15 * '-')