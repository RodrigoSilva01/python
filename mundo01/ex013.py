salario = float(input('Qual o salário: R$'))
aumento = float(input('De quanto será o aumento(%): '))
v_aumento = salario * aumento / 100
final = salario + v_aumento

print('-'*70)
print(f'O salário do funcionário é de R${salario:.2f}, e receberá um aumento de {aumento:.0f}%.')
print(f'O valor do aumento é de R${v_aumento:.2f}.')
print(f'O valor final do aumento é de R${final:.2f}.')
print('-'*70)