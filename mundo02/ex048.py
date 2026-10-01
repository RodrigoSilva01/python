soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f' a soma de todos os {cont} valores que são impares e multiplos de 3 é {soma}')
print('FIM!')
