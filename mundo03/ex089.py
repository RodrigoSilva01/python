ficha = []

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 30)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break

    if opcao <= len(ficha) - 1:
        print(f'As notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
    else:
        print('Aluno não encontrado. Tente novamente.')
    print('-' * 30)

print('<<< VOLTE SEMPRE >>>')
