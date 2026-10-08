num = int(input('Insira um número: '))
num_org = num
resultado = 1
while num > 1:
    resultado = resultado * num
    num = num - 1
print(f'{num_org}! é igual a {resultado}')
