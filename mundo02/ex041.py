from datetime import date

atual = date.today().year
nascimento = int(input('Insira seu ano de nascimento: '))
idade = atual - nascimento
print(f'Você nasceu no ano de {nascimento}')

if idade <= 9:
    print(f'Sua idade é de {idade} anos, sua categoria é MIRIM!')
elif idade <= 14:
    print(f'Sua idade é de {idade} anos, sua categoria é INFANTIL!')
elif idade <= 19:
    print(f'Sua idade é de {idade} anos, sua categoria é JUNIOR!')
elif idade <= 25:
    print(f'Sua idade é de {idade} anos, Sua categoria é SÊNIOR!')
else:
    print(f'Sua idade é de {idade} anos, sua categoria é MASTER!')
