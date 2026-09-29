from math import sqrt

num = int(input('Digite um número: '))

if num <= 1:
    primo = False
else:
    primo = True
    limite = int(sqrt(num)) + 1
    for c in range(2, limite):
        if num % c == 0: 
            primo = False
            break
if primo:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
