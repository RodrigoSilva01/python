salary = float(input('Qual o salário atual: '))
up_1250 = salary * 10 / 100
dw_1250 = salary * 15 / 100

if salary > 1250:
    print(f'Seu salário é de R${salary:.2f} e teve um aumento de 10%, passando para R${salary + up_1250:.2f}')
else:
    print(f'Seu salário é de R${salary:.2f} e teve um aumento de 15%, passando para R${salary + dw_1250:.2f"}')
