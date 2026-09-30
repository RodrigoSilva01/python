idade_menor = 0
idade_maior = 0
for _ in range(1, 8):
    idade = int(input('Insira sua idade: '))
    if idade >= 18:
        idade_maior = idade_maior + 1
    else:
        idade_menor = idade_menor + 1

print(f'Existem {idade_maior} maiores de idade!')
print(f'E existem {idade_menor} menores de idade!')
