from time import sleep

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('Os valores inseridos podem se tornar um triângulo?')
print('Calculando...')
sleep(1.5)

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(f'Sim, os valores podem ser um triângulo, formando um triangulo Equilátero.')
    elif a == b or b == c or c == a: 
        print(f'Sim, os valores podem ser um triângulo, formando um triangulo isósceles.')
    else:
        print(f'Sim, os valores podem ser um triângulo, formando um triangulo Escaleno.')
else:
    print(f'Não é possivel formar um triângulo com os lados A{a}, B{b} e C{c}.')
