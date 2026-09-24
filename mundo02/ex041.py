idade = int(input('Insira sua idade: '))

if idade <= 9:
    print(f'Sua idade é de {idade} anos, sua categoria é MIRIM!')
elif 9 < idade <= 14:
    print(f'Sua idade é de {idade} anos, sua categoria é INFANTIL!')
elif 14 < idade <= 19:
    print(f'Sua idade é de {idade} anos, sua categoria é JUNIOR!')
elif 19 < idade <= 20:
    print(f'Sua idade é de {idade} anos, Sua categoria é SÊNIOR!')
else:
    print(f'Sua idade é de {idade} anos, sua categoria é MASTER!')
