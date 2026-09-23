from time import sleep

a = float(input('Insira um valor: '))
b = float(input('Insira um valor: '))
c = float(input('Insira um valor: '))

print('Os números inseridos podem se tornar um triângulo?')
print('Calculando...')
sleep(1.5)
if a + b > c and a + c > b and b + c > a:
    print('Sim, os números inseridos podem ser um triângulo')
else:
    print('Não, os números inseridos não podem ser um triangulo')
