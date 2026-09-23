n1 = float(input('Insira a nota: '))
n2 = float(input('Insira a nota: '))
m = (n1 + n2) / 2

print(f'A media da turma é {m:.1f}')

if m >= 6:
    print('Você está acima da média, parabéns!')
else:
    print('Você está de abaixo da média, estude mais!')
