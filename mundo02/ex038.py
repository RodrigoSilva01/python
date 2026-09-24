n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 > n2:
    print('O primeiro valor é maior e o segundo menor!')
elif n1 < n2:
    print('O segundo valor é maior e o primeiro menor!')
else:
    print('Não existe valor maior, os dois são iguais!')
