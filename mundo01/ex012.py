v_org = float(input('Qual o valor do produto: '))
desconto = float(input('De quanto é o desconto aplicado: '))
v_desconto = v_org * desconto / 100
final = v_org - (v_org * desconto / 100)

print(f'O produto custava R${v_org} antes da promoção.')
print(f'Com o desconto aplicado de {desconto}% temos um desconto de R${v_desconto:.2f}.')
print(f'Portanto o valor final é de R${final:.2f}.')