import math

oposto = float(input('digite um valor: '))
adjacente = float(input('digite um valor: '))
hipotenusa = math.hypot(oposto, adjacente)

print(f'a hipotenusa do cateto oposto {oposto} e do cateto adjacente {adjacente} é igual a {hipotenusa:.2f}.')




"""""
cateto_op = float(input('Digite um número: '))
cateto_ad = float(input('Digite um número: '))
hipotenusa = (cateto_op ** 2 + cateto_ad ** 2) ** 0.5

print(f'O cateto oposto e o cateto adjacente são respectivamente {cateto_op} e {cateto_ad}.')
print(f'Temos então que a hipotenusa é igual a: {hipotenusa:.2f}')
"""""